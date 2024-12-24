# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
import uuid
from typing import List, Optional, Tuple, Union

from llama_stack_client import LlamaStackClient
from llama_stack_client.types import ToolResponseMessage, UserMessage
from llama_stack_client.types.agent_create_params import AgentConfig
from llama_stack_client.types.custom_tool_def_param import Parameter
from llama_stack_client.types.memory_insert_params import Document
from llama_stack_client.types.tool_def_param import CustomToolDefParam
from llama_stack_client.types.tool_group_def_param import UserDefinedToolGroupDef

from .custom_tool import CustomTool


class Agent:
    def __init__(
        self,
        client: LlamaStackClient,
        agent_config: AgentConfig,
        custom_tools: Tuple[CustomTool] = (),
        memory_bank_id: Optional[str] = None,
    ):
        self.client = client
        self.agent_config = agent_config
        self.agent_id = self._create_agent(agent_config)
        self.custom_tools = {t.get_name(): t for t in custom_tools}
        self.sessions = []
        self.memory_bank_id = memory_bank_id

    @classmethod
    def with_memory(
        cls,
        client: LlamaStackClient,
        agent_config: AgentConfig,
        custom_tools: Tuple[CustomTool] = (),
        memory_bank_id: Optional[str] = None,
    ) -> "Agent":
        if memory_bank_id is None:
            memory_bank_id = "memory_bank_" + str(uuid.uuid4())
            embedding_models = [
                m.identifier
                for m in client.models.list()
                if m.model_type == "embedding"
            ]
            if len(embedding_models) == 0:
                raise ValueError("No embedding model found")
            embedding_model = embedding_models[0]
            client.memory_banks.register(
                memory_bank_id=memory_bank_id,
                params={
                    "memory_bank_type": "vector",
                    "embedding_model": embedding_model,
                    "chunk_size_in_tokens": 512,
                    "overlap_size_in_tokens": 64,
                },
            )
        # find the memory runtime provider
        providers = client.providers.list()
        if providers.get("tool_runtime") is None:
            raise ValueError("Tool runtime provider not found")
        memory_runtime_providers = [
            p.provider_id
            for p in providers.get("tool_runtime")
            if p.provider_type == "inline::memory-runtime"
        ]
        if len(memory_runtime_providers) == 0:
            raise ValueError("Memory runtime provider not found")
        memory_runtime_provider = memory_runtime_providers[0]
        tool_name = "memory-tool" + str(uuid.uuid4())
        client.toolgroups.register(
            tool_group_id="memory_group",
            tool_group=UserDefinedToolGroupDef(
                type="user_defined",
                tools=[
                    CustomToolDefParam(
                        type="custom",
                        name=tool_name,
                        description="Memory tool to retrieve memory from a memory bank based on context of the input messages and attachments",
                        parameters=[
                            Parameter(
                                name="input_messages",
                                description="Input messages for which to retrieve memory",
                                required=True,
                                parameter_type="list",
                            ),
                        ],
                        metadata={
                            "config": {
                                "memory_bank_configs": [
                                    {"bank_id": memory_bank_id, "type": "vector"}
                                ]
                            }
                        },
                    )
                ],
            ),
            provider_id=memory_runtime_provider,
        )
        agent_config["preprocessing_tools"] = [tool_name]
        return cls(client, agent_config, custom_tools, memory_bank_id)

    def _create_agent(self, agent_config: AgentConfig) -> int:
        agentic_system_create_response = self.client.agents.create(
            agent_config=agent_config,
        )
        self.agent_id = agentic_system_create_response.agent_id
        return self.agent_id

    def create_session(self, session_name: str) -> int:
        agentic_system_create_session_response = self.client.agents.session.create(
            agent_id=self.agent_id,
            session_name=session_name,
        )
        self.session_id = agentic_system_create_session_response.session_id
        self.sessions.append(self.session_id)
        return self.session_id

    def _has_tool_call(self, chunk):
        if chunk.event.payload.event_type != "turn_complete":
            return False
        message = chunk.event.payload.turn.output_message
        if message.stop_reason == "out_of_tokens":
            return False
        return len(message.tool_calls) > 0

    def _run_tool(self, chunk):
        message = chunk.event.payload.turn.output_message
        tool_call = message.tool_calls[0]
        if tool_call.tool_name not in self.custom_tools:
            return ToolResponseMessage(
                call_id=tool_call.call_id,
                tool_name=tool_call.tool_name,
                content=f"Unknown tool `{tool_call.tool_name}` was called.",
                role="ipython",
            )
        tool = self.custom_tools[tool_call.tool_name]
        result_messages = tool.run([message])
        next_message = result_messages[0]
        return next_message

    def create_turn(
        self,
        messages: List[Union[UserMessage, ToolResponseMessage]],
        session_id: Optional[str] = None,
    ):
        response = self.client.agents.turn.create(
            agent_id=self.agent_id,
            # use specified session_id or last session created
            session_id=session_id or self.session_id[-1],
            messages=messages,
            stream=True,
        )
        for chunk in response:
            if hasattr(chunk, "error"):
                yield chunk
                return
            elif not self._has_tool_call(chunk):
                yield chunk
            else:
                next_message = self._run_tool(chunk)
                yield next_message

    def add_document(self, document: Document):
        if self.memory_bank_id is None:
            raise ValueError("Memory bank is not set")
        self.client.memory.insert(
            bank_id=self.memory_bank_id,
            documents=[document],
        )

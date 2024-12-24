# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..inference_step import InferenceStep
from ..shared.tool_call import ToolCall
from ..shield_call_step import ShieldCallStep
from ..shared.attachment import Attachment
from ..shared.user_message import UserMessage
from ..tool_execution_step import ToolExecutionStep
from ..memory_retrieval_step import MemoryRetrievalStep
from ..shared.interleaved_content import InterleavedContent
from ..shared.tool_response_message import ToolResponseMessage

__all__ = ["Turn", "InputMessage", "OutputMessage", "Step"]

InputMessage: TypeAlias = Union[UserMessage, ToolResponseMessage]


class OutputMessage(BaseModel):
    content: InterleavedContent

    role: Literal["assistant"]

    stop_reason: Literal["end_of_turn", "end_of_message", "out_of_tokens"]

    tool_calls: List[ToolCall]


Step: TypeAlias = Union[InferenceStep, ToolExecutionStep, ShieldCallStep, MemoryRetrievalStep]


class Turn(BaseModel):
    input_messages: List[InputMessage]

    output_attachments: List[Attachment]

    output_message: OutputMessage

    session_id: str

    started_at: datetime

    steps: List[Step]

    turn_id: str

    completed_at: Optional[datetime] = None

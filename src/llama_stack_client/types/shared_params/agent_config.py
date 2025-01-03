# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .sampling_params import SamplingParams

__all__ = ["AgentConfig", "ClientTool", "ClientToolParameter", "Tool", "ToolUnionMember1"]


class ClientToolParameter(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    parameter_type: Required[str]

    required: Required[bool]

    default: Union[bool, float, str, Iterable[object], object, None]


class ClientTool(TypedDict, total=False):
    description: Required[str]

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    name: Required[str]

    parameters: Required[Iterable[ClientToolParameter]]

    type: Required[Literal["user_defined"]]

    tool_prompt_format: Literal["json", "function_tag", "python_list"]
    """
    `json` -- Refers to the json format for calling tools. The json format takes the
    form like { "type": "function", "function" : { "name": "function_name",
    "description": "function_description", "parameters": {...} } }

    `function_tag` -- This is an example of how you could define your own user
    defined format for making tool calls. The function_tag format looks like this,
    <function=function_name>(parameters)</function>

    The detailed prompts for each of these formats are added to llama cli
    """


class ToolUnionMember1(TypedDict, total=False):
    args: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    name: Required[str]


Tool: TypeAlias = Union[str, ToolUnionMember1]


class AgentConfig(TypedDict, total=False):
    enable_session_persistence: Required[bool]

    instructions: Required[str]

    max_infer_iters: Required[int]

    model: Required[str]

    client_tools: Iterable[ClientTool]

    input_shields: List[str]

    output_shields: List[str]

    sampling_params: SamplingParams

    tool_choice: Literal["auto", "required"]

    tool_prompt_format: Literal["json", "function_tag", "python_list"]
    """
    `json` -- Refers to the json format for calling tools. The json format takes the
    form like { "type": "function", "function" : { "name": "function_name",
    "description": "function_description", "parameters": {...} } }

    `function_tag` -- This is an example of how you could define your own user
    defined format for making tool calls. The function_tag format looks like this,
    <function=function_name>(parameters)</function>

    The detailed prompts for each of these formats are added to llama cli
    """

    tools: List[Tool]

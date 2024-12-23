# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .sampling_params import SamplingParams

__all__ = ["AgentConfig"]


class AgentConfig(BaseModel):
    enable_session_persistence: bool

    instructions: str

    max_infer_iters: int

    model: str

    available_tools: Optional[List[str]] = None

    input_shields: Optional[List[str]] = None

    output_shields: Optional[List[str]] = None

    preprocessing_tools: Optional[List[str]] = None

    sampling_params: Optional[SamplingParams] = None

    tool_choice: Optional[Literal["auto", "required"]] = None

    tool_prompt_format: Optional[Literal["json", "function_tag", "python_list"]] = None
    """
    `json` -- Refers to the json format for calling tools. The json format takes the
    form like { "type": "function", "function" : { "name": "function_name",
    "description": "function_description", "parameters": {...} } }

    `function_tag` -- This is an example of how you could define your own user
    defined format for making tool calls. The function_tag format looks like this,
    <function=function_name>(parameters)</function>

    The detailed prompts for each of these formats are added to llama cli
    """

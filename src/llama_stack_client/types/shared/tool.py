# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .tool_parameter import ToolParameter

__all__ = ["Tool"]


class Tool(BaseModel):
    description: str

    identifier: str

    parameters: List[ToolParameter]

    provider_resource_id: str

    tool_group: str

    type: Literal["tool"]

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

    provider_id: Optional[str] = None

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

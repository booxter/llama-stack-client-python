# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["ToolDef", "UserDefinedToolDef", "UserDefinedToolDefParameter", "BuiltInToolDef"]


class UserDefinedToolDefParameter(BaseModel):
    description: str

    name: str

    parameter_type: str

    required: bool

    default: Union[bool, float, str, List[object], object, None] = None


class UserDefinedToolDef(BaseModel):
    description: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    name: str

    parameters: List[UserDefinedToolDefParameter]

    type: Literal["user_defined"]

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


class BuiltInToolDef(BaseModel):
    built_in_type: Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"]

    type: Literal["built_in"]

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


ToolDef: TypeAlias = Union[UserDefinedToolDef, BuiltInToolDef]

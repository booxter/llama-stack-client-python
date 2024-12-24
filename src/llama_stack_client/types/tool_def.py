# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .custom_tool_def import CustomToolDef

__all__ = ["ToolDef", "BuiltInToolDef"]


class BuiltInToolDef(BaseModel):
    built_in_type: Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"]

    type: Literal["built_in"]

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


ToolDef: TypeAlias = Union[CustomToolDef, BuiltInToolDef]

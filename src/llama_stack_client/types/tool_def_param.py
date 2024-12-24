# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .custom_tool_def_param import CustomToolDefParam

__all__ = ["ToolDefParam", "BuiltInToolDef"]


class BuiltInToolDef(TypedDict, total=False):
    built_in_type: Required[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"]]

    type: Required[Literal["built_in"]]

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]


ToolDefParam: TypeAlias = Union[CustomToolDefParam, BuiltInToolDef]

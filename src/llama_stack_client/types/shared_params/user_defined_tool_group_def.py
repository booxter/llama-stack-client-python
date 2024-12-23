# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..tool_def_param import ToolDefParam

__all__ = ["UserDefinedToolGroupDef"]


class UserDefinedToolGroupDef(TypedDict, total=False):
    tools: Required[Iterable[ToolDefParam]]

    type: Required[Literal["user_defined"]]

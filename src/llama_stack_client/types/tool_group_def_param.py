# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .tool_def_param import ToolDefParam
from .shared_params.url import URL

__all__ = ["ToolGroupDefParam", "McpToolGroupDef", "UserDefinedToolGroupDef"]


class McpToolGroupDef(TypedDict, total=False):
    endpoint: Required[URL]

    type: Required[Literal["model_context_protocol"]]


class UserDefinedToolGroupDef(TypedDict, total=False):
    tools: Required[Iterable[ToolDefParam]]

    type: Required[Literal["user_defined"]]


ToolGroupDefParam: TypeAlias = Union[McpToolGroupDef, UserDefinedToolGroupDef]

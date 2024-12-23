# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .mcp_tool_group_def import McpToolGroupDef
from .user_defined_tool_group_def import UserDefinedToolGroupDef

__all__ = ["ToolGroupDef"]

ToolGroupDef: TypeAlias = Union[McpToolGroupDef, UserDefinedToolGroupDef]

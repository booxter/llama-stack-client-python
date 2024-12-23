# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .url import URL

__all__ = ["McpToolGroupDef"]


class McpToolGroupDef(TypedDict, total=False):
    endpoint: Required[URL]

    type: Required[Literal["model_context_protocol"]]

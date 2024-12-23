# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.tool_group_def import ToolGroupDef

__all__ = ["ToolRuntimeDiscoverParams"]


class ToolRuntimeDiscoverParams(TypedDict, total=False):
    tool_group: Required[ToolGroupDef]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

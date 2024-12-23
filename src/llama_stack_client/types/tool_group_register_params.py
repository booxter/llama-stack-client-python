# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.tool_group_def import ToolGroupDef

__all__ = ["ToolGroupRegisterParams"]


class ToolGroupRegisterParams(TypedDict, total=False):
    tool_group: Required[ToolGroupDef]

    tool_group_id: Required[str]

    provider_id: str

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

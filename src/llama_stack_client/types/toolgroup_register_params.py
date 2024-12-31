# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .tool_group_def_param import ToolGroupDefParam

__all__ = ["ToolgroupRegisterParams"]


class ToolgroupRegisterParams(TypedDict, total=False):
    tool_group: Required[ToolGroupDefParam]

    tool_group_id: Required[str]

    provider_id: str

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

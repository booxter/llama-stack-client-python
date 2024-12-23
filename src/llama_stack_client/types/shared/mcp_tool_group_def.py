# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .url import URL
from ..._models import BaseModel

__all__ = ["McpToolGroupDef"]


class McpToolGroupDef(BaseModel):
    endpoint: URL

    type: Literal["model_context_protocol"]

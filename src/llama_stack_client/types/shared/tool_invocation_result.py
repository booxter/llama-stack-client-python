# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .interleaved_content import InterleavedContent

__all__ = ["ToolInvocationResult"]


class ToolInvocationResult(BaseModel):
    content: InterleavedContent

    error_code: Optional[int] = None

    error_message: Optional[str] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel
from .span_with_status import SpanWithStatus

__all__ = ["TelemetryGetSpanTreeResponse"]


class TelemetryGetSpanTreeResponse(BaseModel):
    data: Dict[str, SpanWithStatus]

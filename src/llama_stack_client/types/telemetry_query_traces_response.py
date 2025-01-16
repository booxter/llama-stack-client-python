# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .trace import Trace
from .._models import BaseModel

__all__ = ["TelemetryQueryTracesResponse"]


class TelemetryQueryTracesResponse(BaseModel):
    data: List[Trace]

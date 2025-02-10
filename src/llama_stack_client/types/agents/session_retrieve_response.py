# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .session import Session
from ..._models import BaseModel

__all__ = ["SessionRetrieveResponse", "SessionRetrieveResponseMetric"]


class SessionRetrieveResponseMetric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class SessionRetrieveResponse(Session):
    metrics: Optional[List[SessionRetrieveResponseMetric]] = None

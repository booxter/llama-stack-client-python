# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .session import Session
from ..._models import BaseModel

__all__ = ["SessionRetrieveResponse", "Metric"]


class Metric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class SessionRetrieveResponse(BaseModel):
    data: Session
    """A single session of an interaction with an Agentic System."""

    metrics: Optional[List[Metric]] = None

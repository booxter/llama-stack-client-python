# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["JobStatusResponse", "JobStatus", "JobStatusMetric", "Metrics", "MetricsMetric"]


class JobStatusMetric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class JobStatus(BaseModel):
    metrics: Optional[List[JobStatusMetric]] = None


class MetricsMetric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class Metrics(BaseModel):
    metrics: Optional[List[MetricsMetric]] = None


JobStatusResponse: TypeAlias = Union[JobStatus, Metrics]

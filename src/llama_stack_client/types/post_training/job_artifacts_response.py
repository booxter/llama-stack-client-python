# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "JobArtifactsResponse",
    "PostTrainingJobArtifactsResponse",
    "PostTrainingJobArtifactsResponseMetric",
    "Metrics",
    "MetricsMetric",
]


class PostTrainingJobArtifactsResponseMetric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class PostTrainingJobArtifactsResponse(BaseModel):
    checkpoints: List[object]

    job_uuid: str

    metrics: Optional[List[PostTrainingJobArtifactsResponseMetric]] = None


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


JobArtifactsResponse: TypeAlias = Union[PostTrainingJobArtifactsResponse, Metrics]

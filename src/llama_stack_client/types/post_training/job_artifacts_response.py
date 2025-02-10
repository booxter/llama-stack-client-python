# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["JobArtifactsResponse", "Data", "Metric"]


class Data(BaseModel):
    checkpoints: List[object]

    job_uuid: str


class Metric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class JobArtifactsResponse(BaseModel):
    data: Optional[Data] = None
    """Artifacts of a finetuning job."""

    metrics: Optional[List[Metric]] = None

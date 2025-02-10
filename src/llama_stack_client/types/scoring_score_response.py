# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.scoring_result import ScoringResult

__all__ = ["ScoringScoreResponse", "Data", "Metric"]


class Data(BaseModel):
    results: Dict[str, ScoringResult]


class Metric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class ScoringScoreResponse(BaseModel):
    data: Data

    metrics: Optional[List[Metric]] = None

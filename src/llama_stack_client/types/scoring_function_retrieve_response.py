# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .scoring_fn import ScoringFn

__all__ = [
    "ScoringFunctionRetrieveResponse",
    "ScoringFunctionsScoringFn",
    "ScoringFunctionsScoringFnMetric",
    "Metrics",
    "MetricsMetric",
]


class ScoringFunctionsScoringFnMetric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class ScoringFunctionsScoringFn(ScoringFn):
    metrics: Optional[List[ScoringFunctionsScoringFnMetric]] = None


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


ScoringFunctionRetrieveResponse: TypeAlias = Union[ScoringFunctionsScoringFn, Optional[Metrics]]

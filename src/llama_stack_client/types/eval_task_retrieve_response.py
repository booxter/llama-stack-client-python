# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .eval_task import EvalTask

__all__ = ["EvalTaskRetrieveResponse", "EvalTasksEvalTask", "EvalTasksEvalTaskMetric", "Metrics", "MetricsMetric"]


class EvalTasksEvalTaskMetric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class EvalTasksEvalTask(EvalTask):
    metrics: Optional[List[EvalTasksEvalTaskMetric]] = None


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


EvalTaskRetrieveResponse: TypeAlias = Union[EvalTasksEvalTask, Optional[Metrics]]

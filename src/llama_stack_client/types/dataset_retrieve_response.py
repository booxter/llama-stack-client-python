# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.url import URL
from .shared.param_type import ParamType

__all__ = ["DatasetRetrieveResponse", "Dataset", "DatasetMetric", "Metrics", "MetricsMetric"]


class DatasetMetric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class Dataset(BaseModel):
    dataset_schema: Dict[str, ParamType]

    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    provider_resource_id: str

    type: Literal["dataset"]

    url: URL

    metrics: Optional[List[DatasetMetric]] = None


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


DatasetRetrieveResponse: TypeAlias = Union[Dataset, Metrics]

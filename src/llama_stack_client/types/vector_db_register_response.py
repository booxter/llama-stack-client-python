# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VectorDBRegisterResponse", "Metric"]


class Metric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class VectorDBRegisterResponse(BaseModel):
    embedding_dimension: int

    embedding_model: str

    identifier: str

    provider_id: str

    provider_resource_id: str

    type: Literal["vector_db"]

    metrics: Optional[List[Metric]] = None

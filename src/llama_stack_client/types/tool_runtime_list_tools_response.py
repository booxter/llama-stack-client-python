# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .tool_def import ToolDef

__all__ = ["ToolRuntimeListToolsResponse", "ToolRuntimeListToolsResponseMetric"]


class ToolRuntimeListToolsResponseMetric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class ToolRuntimeListToolsResponse(ToolDef):
    metrics: Optional[List[ToolRuntimeListToolsResponseMetric]] = None

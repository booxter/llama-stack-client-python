# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .route_info import RouteInfo

__all__ = ["RouteListResponse"]


class RouteListResponse(BaseModel):
    data: List[RouteInfo]

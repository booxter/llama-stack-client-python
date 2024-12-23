# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from ..tool_def import ToolDef

__all__ = ["UserDefinedToolGroupDef"]


class UserDefinedToolGroupDef(BaseModel):
    tools: List[ToolDef]

    type: Literal["user_defined"]

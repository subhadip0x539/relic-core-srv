from .response import Response
from pydantic import BaseModel
from typing import Optional


class GetFeaturesResponseBodyItem(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    type: str
    enabled: bool
    value: Optional[str | int | float] = None


GetFeaturesResponseBody = list[GetFeaturesResponseBodyItem]


GetFeaturesResponse = Response[GetFeaturesResponseBody]

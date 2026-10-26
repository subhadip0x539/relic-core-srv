from .response import Response
from pydantic import BaseModel
from typing import Optional
from .request import RequestBodyFilters


class GetFlagsRequestBody(BaseModel):
    filters: Optional[RequestBodyFilters] = []


class GetFlagsResponseBodyItem(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    type: str
    enabled: bool
    value: Optional[str | int | float] = None


GetFlagsResponseBody = list[GetFlagsResponseBodyItem]


GetFlagsResponse = Response[GetFlagsResponseBody]


class PostFlagRequestBody(BaseModel):
    name: str
    description: Optional[str] = None
    type: str
    enabled: bool
    value: Optional[str | int | float] = None
    service_id: str
    environment_id: str
    workspace_id: str


PostFlagResponse = Response[str]


class PatchFlagRequestBody(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    enabled: Optional[bool] = None
    value: Optional[str | int | float] = None


PatchFlagResponse = Response[None]

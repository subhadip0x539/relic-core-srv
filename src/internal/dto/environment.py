from .response import Response
from pydantic import BaseModel
from typing import Optional
from .request import RequestBodyFilters


class GetEnvironmentsRequestBody(BaseModel):
    filters: Optional[RequestBodyFilters] = []


class GetEnvironmentsResponseResponseBodyItem(BaseModel):
    id: str
    name: str
    color: str
    workspace_id: str


GetEnvironmentsResponseResponseBody = list[GetEnvironmentsResponseResponseBodyItem]

GetEnvironmentsResponse = Response[GetEnvironmentsResponseResponseBody]


class PostEnvironmentRequestBody(BaseModel):
    name: str
    color: str
    workspace_id: str


PostEnvironmentResponse = Response[str]

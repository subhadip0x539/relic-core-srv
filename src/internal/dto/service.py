from .response import Response
from pydantic import BaseModel
from .request import RequestBodyFilters
from typing import Optional


class GetServicesRequestBody(BaseModel):
    filters: Optional[RequestBodyFilters] = []


class GetServicesResponseResponseBodyItem(BaseModel):
    id: str
    name: str


GetServicesResponseResponseBody = list[GetServicesResponseResponseBodyItem]

GetServicesResponse = Response[GetServicesResponseResponseBody]


class GetServiceResponseBody(BaseModel):
    id: str
    name: str
    workspace_id: str
    environment_id: str


GetServiceResponse = Response[GetServiceResponseBody]


class PostServiceRequest(BaseModel):
    name: str
    workspace_id: str
    environment_id: str


PostServiceResponse = Response[str]

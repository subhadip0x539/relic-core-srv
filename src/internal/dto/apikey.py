from .response import Response
from pydantic import BaseModel
from typing import Optional
from .request import RequestBodyFilters


class GetApiKeysRequestBody(BaseModel):
    filters: Optional[RequestBodyFilters] = []


class GetApiKeysResponseBodyItemService(BaseModel):
    id: str
    name: str


class GetApiKeysResponseBodyItem(BaseModel):
    id: str
    service: GetApiKeysResponseBodyItemService


GetApiKeysResponseBody = list[GetApiKeysResponseBodyItem]

GetApiKeysResponse = Response[GetApiKeysResponseBody]


class PostApiKeyRequestBody(BaseModel):
    service_id: str


PostApiKeyResponse = Response[str]

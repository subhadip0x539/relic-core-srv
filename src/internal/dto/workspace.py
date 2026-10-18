from .response import Response
from pydantic import BaseModel


class GetWorkspacesResponseResponseBodyItem(BaseModel):
    id: str
    name: str


GetWorkspacesResponseResponseBody = list[GetWorkspacesResponseResponseBodyItem]

GetWorkspacesResponse = Response[GetWorkspacesResponseResponseBody]


class PostWorkspaceRequestBody(BaseModel):
    name: str


PostWorkspaceResponse = Response[str]

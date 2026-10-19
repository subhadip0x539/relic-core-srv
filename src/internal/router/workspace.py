from fastapi import APIRouter, Depends, status
from internal.dto.workspace import (
    GetWorkspacesResponse,
    PostWorkspaceRequestBody,
    PostWorkspaceResponse,
)
from internal.deps.workspace import WorkspaceHandler, get_workspace_handler
from internal.deps.common import Claims, get_claims

router = APIRouter(
    prefix="/workspaces",
)


@router.get("", response_model=GetWorkspacesResponse, response_model_exclude_none=True)
def all(
    claims: Claims = Depends(get_claims),
    hdl: WorkspaceHandler = Depends(get_workspace_handler),
):
    return hdl.all(claims)


@router.post(
    "",
    response_model=PostWorkspaceResponse,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True,
)
def create(
    body: PostWorkspaceRequestBody,
    claims: Claims = Depends(get_claims),
    hdl: WorkspaceHandler = Depends(get_workspace_handler),
):
    return hdl.create(body, claims)

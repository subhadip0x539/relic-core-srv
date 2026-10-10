from fastapi import APIRouter, Depends, status
from internal.dto.workspace import (
    GetWorkspacesResponse,
    PostWorkspaceRequest,
    PostWorkspaceResponse,
)
from internal.deps.workspace import WorkspaceHandler, get_workspace_handler

router = APIRouter(prefix="/workspaces")


@router.get("", response_model=GetWorkspacesResponse, response_model_exclude_none=True)
def all(
    hdl: WorkspaceHandler = Depends(get_workspace_handler),
):
    return hdl.all()


@router.post(
    "",
    response_model=PostWorkspaceResponse,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True,
)
def create(
    request: PostWorkspaceRequest,
    hdl: WorkspaceHandler = Depends(get_workspace_handler),
):
    return hdl.create(request)

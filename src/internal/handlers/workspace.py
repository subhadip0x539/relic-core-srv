from internal.port.workspace import WorkspaceService
from internal.dto.workspace import (
    GetWorkspacesResponse,
    GetWorkspacesResponseResponseBodyItem,
    PostWorkspaceResponse,
    PostWorkspaceRequestBody,
)
from fastapi import HTTPException
from internal.lib.claims import Claims
from internal.domain.auth import Permission
from internal.domain.error import ForbiddenError


class WorkspaceHandler:
    svc: WorkspaceService

    def __init__(self, svc: WorkspaceService):
        self.svc = svc

    def all(self, claims: Claims) -> GetWorkspacesResponse:
        try:
            claims.can(Permission.WORKSPACE_READ)
        except ForbiddenError as exc:
            raise HTTPException(exc.code, exc.message)

        result = self.svc.all()

        response = GetWorkspacesResponse(
            body=[
                GetWorkspacesResponseResponseBodyItem(id=str(r.id), name=r.name)
                for r in result
            ]
        )

        return response

    def create(
        self, body: PostWorkspaceRequestBody, claims: Claims
    ) -> PostWorkspaceResponse:
        try:
            claims.can(Permission.WORKSPACE_CREATE)
        except ForbiddenError as exc:
            raise HTTPException(exc.code, exc.message)

        result = self.svc.create(body.name)

        return PostWorkspaceResponse(
            detail="Workspace created successfully",
            body=result.id,
        )

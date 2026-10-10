from internal.port.workspace import WorkspaceService
from internal.dto.workspace import GetWorkspacesResponse, GetWorkspacesResponseResponseBodyItem, PostWorkspaceResponse, PostWorkspaceRequest

class WorkspaceHandler:
    svc: WorkspaceService

    def __init__(self, svc: WorkspaceService):
        self.svc = svc

    def all(self) -> GetWorkspacesResponse:
        result = self.svc.all()

        response = GetWorkspacesResponse(
            body=[GetWorkspacesResponseResponseBodyItem(id=str(r.id), name=r.name) for r in result]
        )

        return response

    def create(self, request: PostWorkspaceRequest) -> PostWorkspaceResponse:
        result = self.svc.create(request)

        return PostWorkspaceResponse(
            detail="Workspace created successfully",
            body=result.id,
        )
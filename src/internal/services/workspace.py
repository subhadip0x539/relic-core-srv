from internal.port.workspace import WorkspaceService, WorkspaceRepository
from internal.domain.workspace import Workspace
from internal.dto.workspace import PostWorkspaceRequest
from uuid import uuid4


class WorkspaceServiceImpl(WorkspaceService):
    def __init__(self, repo: WorkspaceRepository):
        self.repo = repo

    def all(self) -> list[Workspace]:
        return self.repo.all()

    def create(self, request: PostWorkspaceRequest) -> Workspace:
        payload = Workspace(
            id=str(uuid4()),
            name=request.name,
        )

        return self.repo.create(payload)

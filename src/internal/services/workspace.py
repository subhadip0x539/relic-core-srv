from internal.port.workspace import WorkspaceService, WorkspaceRepository
from internal.domain.workspace import Workspace
from uuid import uuid4


class WorkspaceServiceImpl(WorkspaceService):
    def __init__(self, repo: WorkspaceRepository):
        self.repo = repo

    def all(self) -> list[Workspace]:
        return self.repo.all()

    def create(self, name: str) -> Workspace:
        payload = Workspace(
            id=str(uuid4()),
            name=name,
        )

        return self.repo.create(payload)

from abc import ABC, abstractmethod
from internal.domain.workspace import Workspace
from internal.dto.workspace import PostWorkspaceRequest


class WorkspaceRepository(ABC):
    @abstractmethod
    def all(self) -> list[Workspace]:
        pass

    @abstractmethod
    def create(self, workspace: Workspace) -> Workspace:
        pass


class WorkspaceService(ABC):
    @abstractmethod
    def all(self) -> list[Workspace]:
        pass

    @abstractmethod
    def create(self, request: PostWorkspaceRequest) -> Workspace:
        pass

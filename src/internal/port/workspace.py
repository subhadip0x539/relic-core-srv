from abc import ABC, abstractmethod
from internal.domain.workspace import Workspace


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
    def create(self, name: str) -> Workspace:
        pass

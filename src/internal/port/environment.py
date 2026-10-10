from abc import ABC, abstractmethod
from internal.domain.environment import Environment
from internal.dto.environment import GetEnvironmentsRequestBody, PostEnvironmentRequest
from internal.lib.fc import FC


class EnvironmentRepository(ABC):
    @abstractmethod
    def all(self, fc: FC) -> list[Environment]:
        pass

    @abstractmethod
    def create(self, environment: Environment) -> Environment:
        pass


class EnvironmentService(ABC):
    @abstractmethod
    def all(self, body: GetEnvironmentsRequestBody) -> list[Environment]:
        pass

    @abstractmethod
    def create(self, request: PostEnvironmentRequest) -> Environment:
        pass

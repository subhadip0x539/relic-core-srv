from abc import ABC, abstractmethod
from internal.domain.service import Service
from internal.dto.service import PostServiceRequestBody, GetServicesRequestBody
from internal.lib.fc import FC


class ServiceRepository(ABC):
    @abstractmethod
    def all(self, fc: FC) -> list[Service]:
        pass

    @abstractmethod
    def get(self, service_id: str) -> Service:
        pass

    @abstractmethod
    def create(self, service: Service) -> Service:
        pass


class ServiceService(ABC):
    @abstractmethod
    def all(self, body: GetServicesRequestBody) -> list[Service]:
        pass

    @abstractmethod
    def get(self, service_id: str) -> Service:
        pass

    @abstractmethod
    def create(self, body: PostServiceRequestBody) -> Service:
        pass

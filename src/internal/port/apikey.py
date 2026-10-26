from abc import ABC, abstractmethod
from internal.domain.apikey import ApiKey
from internal.dto.apikey import (
    GetApiKeysRequestBody,
    PostApiKeyRequestBody,
    GetApiKeysResponseBody,
)
from internal.lib.fc import FC


class ApiKeyRepository(ABC):
    @abstractmethod
    def all(self, fc: FC) -> list[ApiKey]:
        pass

    @abstractmethod
    def get(self, api_key: str) -> ApiKey:
        pass

    @abstractmethod
    def create(self, api_key: ApiKey) -> ApiKey:
        pass


class ApiKeyService(ABC):
    @abstractmethod
    def all(self, body: GetApiKeysRequestBody) -> GetApiKeysResponseBody:
        pass

    @abstractmethod
    def create(self, body: PostApiKeyRequestBody) -> ApiKey:
        pass

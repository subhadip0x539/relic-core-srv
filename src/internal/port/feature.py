from abc import ABC, abstractmethod
from internal.domain.feature import Feature
from internal.dto.feature import GetFeaturesResponseBody
from internal.lib.fc import FC


class FeatureRepository(ABC):
    @abstractmethod
    def all(self, fc: FC) -> list[Feature]:
        pass


class FeatureService(ABC):
    @abstractmethod
    def all(self, api_key: str) -> GetFeaturesResponseBody:
        pass

from abc import ABC, abstractmethod
from internal.domain.flag import Flag
from internal.dto.flag import (
    PostFlagRequestBody,
    GetFlagsRequestBody,
    PatchFlagRequestBody,
)
from internal.lib.fc import FC


class FlagRepository(ABC):
    @abstractmethod
    def all(self, fc: FC) -> list[Flag]:
        pass

    @abstractmethod
    def create(self, Flag: Flag) -> Flag:
        pass

    @abstractmethod
    async def update(self, flag_id: str, payload: PatchFlagRequestBody):
        pass


class FlagService(ABC):
    @abstractmethod
    def all(self, body: GetFlagsRequestBody) -> list[Flag]:
        pass

    @abstractmethod
    def create(self, body: PostFlagRequestBody) -> Flag:
        pass

    @abstractmethod
    async def update(self, flag_id: str, request: PatchFlagRequestBody):
        pass

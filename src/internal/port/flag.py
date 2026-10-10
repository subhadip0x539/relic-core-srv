from abc import ABC, abstractmethod
from internal.domain.flag import Flag
from internal.dto.flag import PostFlagRequest, GetFlagsRequestBody, PatchFlagRequest
from internal.lib.fc import FC


class FlagRepository(ABC):
    @abstractmethod
    def all(self, fc: FC) -> list[Flag]:
        pass

    @abstractmethod
    def create(self, Flag: Flag) -> Flag:
        pass

    @abstractmethod
    async def update(self, flag_id: str, payload: PatchFlagRequest):
        pass


class FlagService(ABC):
    @abstractmethod
    def all(self, body: GetFlagsRequestBody) -> list[Flag]:
        pass

    @abstractmethod
    def create(self, request: PostFlagRequest) -> Flag:
        pass

    @abstractmethod
    async def update(self, flag_id: str, request: PatchFlagRequest):
        pass

from internal.port.flag import (
    FlagService,
    FlagRepository,
    GetFlagsRequestBody,
    PatchFlagRequest,
)
from internal.domain.flag import Flag
from internal.dto.flag import PostFlagRequest
from uuid import uuid4
from internal.domain.common import Filter, FilterOperator
from internal.lib.fc import FC


class FlagServiceImpl(FlagService):
    def __init__(
        self,
        repo: FlagRepository,
    ):
        self.repo = repo

    def all(self, body: GetFlagsRequestBody) -> list[Flag]:
        filters: list[Filter] = [
            Filter(field=f.field, operator=FilterOperator(f.operator), value=f.value)
            for f in body.filters or []
        ]

        fc = FC(filters)

        return self.repo.all(fc)

    def create(self, request: PostFlagRequest) -> Flag:
        payload = Flag(
            id=str(uuid4()),
            name=request.name,
            description=request.description,
            type=request.type,
            enabled=request.enabled,
            value=request.value,
            service_id=request.service_id,
            environment_id=request.environment_id,
            workspace_id=request.workspace_id,
        )

        return self.repo.create(payload)

    async def update(self, flag_id: str, request: PatchFlagRequest):
        result = await self.repo.update(flag_id, request)

        return result

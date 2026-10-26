from internal.port.flag import (
    FlagService,
    FlagRepository,
    GetFlagsRequestBody,
    PatchFlagRequestBody,
)
from internal.domain.flag import Flag
from internal.dto.flag import PostFlagRequestBody
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

    def create(self, body: PostFlagRequestBody) -> Flag:
        payload = Flag(
            id=str(uuid4()),
            name=body.name,
            description=body.description,
            type=body.type,
            enabled=body.enabled,
            value=body.value,
            service_id=body.service_id,
            environment_id=body.environment_id,
            workspace_id=body.workspace_id,
        )

        return self.repo.create(payload)

    async def update(self, flag_id: str, request: PatchFlagRequestBody):
        result = await self.repo.update(flag_id, request)

        return result

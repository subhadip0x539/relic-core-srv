from internal.port.flag import FlagService
from internal.dto.flag import (
    GetFlagsResponse,
    GetFlagsResponseBodyItem,
    PostFlagResponse,
    PostFlagRequest,
    GetFlagsRequestBody,
    PatchFlagRequest,
    PatchFlagResponse,
)


class FlagHandler:
    svc: FlagService

    def __init__(self, svc: FlagService):
        self.svc = svc

    def all(self, body: GetFlagsRequestBody) -> GetFlagsResponse:
        result = self.svc.all(body)

        response = GetFlagsResponse(
            body=[
                GetFlagsResponseBodyItem(
                    id=r.id,
                    name=r.name,
                    description=r.description,
                    type=r.type,
                    enabled=r.enabled,
                    value=r.value,
                )
                for r in result
            ]
        )

        return response

    def create(self, request: PostFlagRequest) -> PostFlagResponse:
        result = self.svc.create(request)

        return PostFlagResponse(
            detail="Flag created successfully",
            body=result.id,
        )

    async def update(
        self, flag_id: str, request: PatchFlagRequest
    ) -> PatchFlagResponse:
        await self.svc.update(flag_id, request)

        return PatchFlagResponse(detail="Flag updated successfully", body=None)

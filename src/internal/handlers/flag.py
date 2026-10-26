from internal.port.flag import FlagService
from internal.dto.flag import (
    GetFlagsResponse,
    GetFlagsResponseBodyItem,
    PostFlagResponse,
    PostFlagRequestBody,
    GetFlagsRequestBody,
    PatchFlagRequestBody,
    PatchFlagResponse,
)
from fastapi import HTTPException
from internal.lib.claims import Claims
from internal.domain.auth import Permission
from internal.domain.error import ForbiddenError


class FlagHandler:
    svc: FlagService

    def __init__(self, svc: FlagService):
        self.svc = svc

    def all(self, body: GetFlagsRequestBody, claims: Claims) -> GetFlagsResponse:
        try:
            claims.can(Permission.FLAG_READ)
        except ForbiddenError as exc:
            raise HTTPException(exc.code, exc.message)
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

    def create(self, body: PostFlagRequestBody, claims: Claims) -> PostFlagResponse:
        try:
            claims.can(Permission.FLAG_CREATE)
        except ForbiddenError as exc:
            raise HTTPException(exc.code, exc.message)

        result = self.svc.create(body)

        return PostFlagResponse(
            detail="Flag created successfully",
            body=result.id,
        )

    async def update(
        self, flag_id: str, body: PatchFlagRequestBody, claims: Claims
    ) -> PatchFlagResponse:
        try:
            claims.can(Permission.FLAG_CREATE)
        except ForbiddenError as exc:
            raise HTTPException(exc.code, exc.message)
        await self.svc.update(flag_id, body)

        return PatchFlagResponse(detail="Flag updated successfully", body=None)

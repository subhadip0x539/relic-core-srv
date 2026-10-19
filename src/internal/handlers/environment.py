from internal.port.environment import EnvironmentService
from internal.dto.environment import (
    GetEnvironmentsRequestBody,
    GetEnvironmentsResponse,
    GetEnvironmentsResponseResponseBodyItem,
    PostEnvironmentResponse,
    PostEnvironmentRequestBody,
)
from fastapi import HTTPException
from internal.lib.claims import Claims
from internal.domain.auth import Permission
from internal.domain.error import ForbiddenError


class EnvironmentHandler:
    svc: EnvironmentService

    def __init__(self, svc: EnvironmentService):
        self.svc = svc

    def all(
        self, body: GetEnvironmentsRequestBody, claims: Claims
    ) -> GetEnvironmentsResponse:
        try:
            claims.can(Permission.ENVIRONMENT_READ)
        except ForbiddenError as exc:
            raise HTTPException(exc.code, exc.message)

        result = self.svc.all(body)

        response = GetEnvironmentsResponse(
            body=[
                GetEnvironmentsResponseResponseBodyItem(
                    id=str(r.id),
                    name=r.name,
                    color=r.color,
                    workspace_id=r.workspace_id,
                )
                for r in result
            ]
        )

        return response

    def create(
        self, body: PostEnvironmentRequestBody, claims: Claims
    ) -> PostEnvironmentResponse:
        try:
            claims.can(Permission.ENVIRONMENT_CREATE)
        except ForbiddenError as exc:
            raise HTTPException(exc.code, exc.message)

        result = self.svc.create(body.name, body.color, body.workspace_id)

        return PostEnvironmentResponse(
            detail="Environment created successfully",
            body=result.id,
        )

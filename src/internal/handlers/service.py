from internal.port.service import ServiceService
from internal.dto.service import (
    GetServicesResponse,
    GetServicesResponseResponseBodyItem,
    PostServiceRequestBody,
    PostServiceResponse,
    GetServicesRequestBody,
    GetServiceResponse,
    GetServiceResponseBody,
)
from fastapi import HTTPException
from internal.lib.claims import Claims
from internal.domain.auth import Permission
from internal.domain.error import ForbiddenError


class ServiceHandler:
    svc: ServiceService

    def __init__(self, svc: ServiceService):
        self.svc = svc

    def all(self, body: GetServicesRequestBody, claims: Claims) -> GetServicesResponse:
        try:
            claims.can(Permission.SERVICE_READ)
        except ForbiddenError as exc:
            raise HTTPException(exc.code, exc.message)

        result = self.svc.all(body)

        response = GetServicesResponse(
            body=[
                GetServicesResponseResponseBodyItem(id=str(r.id), name=r.name)
                for r in result
            ]
        )

        return response

    def get(self, service_id: str, claims: Claims) -> GetServiceResponse:
        try:
            claims.can(Permission.SERVICE_READ)
        except ForbiddenError as exc:
            raise HTTPException(exc.code, exc.message)

        result = self.svc.get(service_id)

        response = GetServiceResponse(
            body=GetServiceResponseBody(
                id=result.id,
                name=result.name,
                workspace_id=result.workspace_id,
                environment_id=result.environment_id,
            )
        )

        return response

    def create(
        self, body: PostServiceRequestBody, claims: Claims
    ) -> PostServiceResponse:
        try:
            claims.can(Permission.SERVICE_CREATE)
        except ForbiddenError as exc:
            raise HTTPException(exc.code, exc.message)

        result = self.svc.create(body)

        return PostServiceResponse(
            detail="Service created successfully",
            body=result.id,
        )

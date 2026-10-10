from internal.port.service import ServiceService
from internal.dto.service import (
    GetServicesResponse,
    GetServicesResponseResponseBodyItem,
    PostServiceRequest,
    PostServiceResponse,
    GetServicesRequestBody,
    GetServiceResponse,
    GetServiceResponseBody,
)


class ServiceHandler:
    svc: ServiceService

    def __init__(self, svc: ServiceService):
        self.svc = svc

    def all(self, body: GetServicesRequestBody) -> GetServicesResponse:
        result = self.svc.all(body)

        response = GetServicesResponse(
            body=[
                GetServicesResponseResponseBodyItem(id=str(r.id), name=r.name)
                for r in result
            ]
        )

        return response

    def get(self, service_id: str) -> GetServiceResponse:
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

    def create(self, request: PostServiceRequest) -> PostServiceResponse:
        result = self.svc.create(request)

        return PostServiceResponse(
            detail="Service created successfully",
            body=result.id,
        )

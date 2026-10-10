from internal.port.environment import EnvironmentService
from internal.dto.environment import (
    GetEnvironmentsRequestBody,
    GetEnvironmentsResponse,
    GetEnvironmentsResponseResponseBodyItem,
    PostEnvironmentResponse,
    PostEnvironmentRequest,
)


class EnvironmentHandler:
    svc: EnvironmentService

    def __init__(self, svc: EnvironmentService):
        self.svc = svc

    def all(self, body: GetEnvironmentsRequestBody) -> GetEnvironmentsResponse:
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

    def create(self, request: PostEnvironmentRequest) -> PostEnvironmentResponse:
        result = self.svc.create(request)

        return PostEnvironmentResponse(
            detail="Environment created successfully",
            body=result.id,
        )

from internal.port.service import ServiceService, ServiceRepository
from internal.domain.service import Service
from internal.dto.service import PostServiceRequest, GetServicesRequestBody
from uuid import uuid4
from internal.domain.common import Filter, FilterOperator
from internal.lib.fc import FC


class ServiceServiceImpl(ServiceService):
    def __init__(self, repo: ServiceRepository):
        self.repo = repo

    def all(self, body: GetServicesRequestBody) -> list[Service]:
        filters: list[Filter] = [
            Filter(field=f.field, operator=FilterOperator(f.operator), value=f.value)
            for f in body.filters or []
        ]
        fc = FC(filters)
        return self.repo.all(fc)

    def get(self, service_id: str) -> Service:
        return self.repo.get(service_id)

    def create(self, request: PostServiceRequest) -> Service:
        payload = Service(
            id=str(uuid4()),
            workspace_id=request.workspace_id,
            environment_id=request.environment_id,
            name=request.name,
        )

        return self.repo.create(payload)

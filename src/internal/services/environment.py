from internal.port.environment import EnvironmentService, EnvironmentRepository
from internal.domain.environment import Environment
from internal.dto.environment import GetEnvironmentsRequestBody
from uuid import uuid4
from internal.domain.common import Filter, FilterOperator
from internal.lib.fc import FC


class EnvironmentServiceImpl(EnvironmentService):
    def __init__(self, repo: EnvironmentRepository):
        self.repo = repo

    def all(self, body: GetEnvironmentsRequestBody) -> list[Environment]:
        filters: list[Filter] = [
            Filter(field=f.field, operator=FilterOperator(f.operator), value=f.value)
            for f in body.filters or []
        ]

        fc = FC(filters)

        return self.repo.all(fc)

    def create(self, name: str, color: str, workspace_id: str) -> Environment:
        payload = Environment(
            id=str(uuid4()),
            name=name,
            workspace_id=workspace_id,
            color=color,
        )

        return self.repo.create(payload)

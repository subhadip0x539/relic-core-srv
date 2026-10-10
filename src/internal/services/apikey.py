from internal.port.apikey import ApiKeyService, ApiKeyRepository
from internal.port.service import ServiceRepository
from internal.domain.apikey import ApiKey
from internal.dto.apikey import (
    GetApiKeysRequestBody,
    PostApiKeyRequest,
    GetApiKeysResponseBody,
    GetApiKeysResponseBodyItem,
    GetApiKeysResponseBodyItemService,
)
from uuid import uuid4
from internal.domain.common import Filter, FilterOperator
from internal.lib.fc import FC


class ApiKeyServiceImpl(ApiKeyService):
    def __init__(self, api_key_repo: ApiKeyRepository, service_repo: ServiceRepository):
        self.api_key_repo = api_key_repo
        self.service_repo = service_repo

    def all(self, body: GetApiKeysRequestBody) -> GetApiKeysResponseBody:
        filters: list[Filter] = [
            Filter(field=f.field, operator=FilterOperator(f.operator), value=f.value)
            for f in body.filters or []
        ]

        fc = FC(filters)

        ak = self.api_key_repo.all(fc)
        sr = self.service_repo.all(FC())
        so = {s.id: s for s in sr}

        result = [
            GetApiKeysResponseBodyItem(
                id=a.id,
                service=GetApiKeysResponseBodyItemService(
                    id=a.service_id,
                    name=so[a.service_id].name,
                ),
            )
            for a in ak
        ]

        return result

    def create(self, request: PostApiKeyRequest) -> ApiKey:
        service = self.service_repo.get(request.service_id)

        payload = ApiKey(
            id=str(uuid4()),
            workspace_id=service.workspace_id,
            environment_id=service.environment_id,
            service_id=request.service_id,
        )

        return self.api_key_repo.create(payload)

from internal.port.apikey import ApiKeyService
from internal.dto.apikey import (
    GetApiKeysRequestBody,
    GetApiKeysResponse,
    PostApiKeyResponse,
    PostApiKeyRequest,
)


class ApiKeyHandler:
    svc: ApiKeyService

    def __init__(self, svc: ApiKeyService):
        self.svc = svc

    def all(self, body: GetApiKeysRequestBody) -> GetApiKeysResponse:
        result = self.svc.all(body)

        response = GetApiKeysResponse(body=result)

        return response

    def create(self, request: PostApiKeyRequest) -> PostApiKeyResponse:
        result = self.svc.create(request)

        return PostApiKeyResponse(
            detail="API Key created successfully",
            body=result.id,
        )

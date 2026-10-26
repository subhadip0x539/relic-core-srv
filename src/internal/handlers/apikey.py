from internal.port.apikey import ApiKeyService
from internal.dto.apikey import (
    GetApiKeysRequestBody,
    GetApiKeysResponse,
    PostApiKeyResponse,
    PostApiKeyRequestBody,
)
from fastapi import HTTPException
from internal.lib.claims import Claims
from internal.domain.auth import Permission
from internal.domain.error import ForbiddenError


class ApiKeyHandler:
    svc: ApiKeyService

    def __init__(self, svc: ApiKeyService):
        self.svc = svc

    def all(self, body: GetApiKeysRequestBody, claims: Claims) -> GetApiKeysResponse:
        try:
            claims.can(Permission.API_KEY_READ)
        except ForbiddenError as exc:
            raise HTTPException(exc.code, exc.message)

        result = self.svc.all(body)

        response = GetApiKeysResponse(body=result)

        return response

    def create(self, body: PostApiKeyRequestBody, claims: Claims) -> PostApiKeyResponse:
        try:
            claims.can(Permission.API_KEY_CREATE)
        except ForbiddenError as exc:
            raise HTTPException(exc.code, exc.message)

        result = self.svc.create(body)

        return PostApiKeyResponse(
            detail="API Key created successfully",
            body=result.id,
        )

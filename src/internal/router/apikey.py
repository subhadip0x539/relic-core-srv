from fastapi import APIRouter, Depends, status
from internal.dto.apikey import (
    GetApiKeysRequestBody,
    GetApiKeysResponse,
    PostApiKeyRequestBody,
    PostApiKeyResponse,
)
from internal.deps.apikey import ApiKeyHandler, get_api_key_handler
from internal.deps.common import Claims, get_claims

router = APIRouter(prefix="/api-keys")


@router.post(
    "/all", response_model=GetApiKeysResponse, response_model_exclude_none=True
)
def all(
    body: GetApiKeysRequestBody,
    claims: Claims = Depends(get_claims),
    hdl: ApiKeyHandler = Depends(get_api_key_handler),
):
    return hdl.all(body, claims)


@router.post(
    "",
    response_model=PostApiKeyResponse,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True,
)
def create(
    body: PostApiKeyRequestBody,
    claims: Claims = Depends(get_claims),
    hdl: ApiKeyHandler = Depends(get_api_key_handler),
):
    return hdl.create(body, claims)

from fastapi import APIRouter, Depends, status
from internal.dto.apikey import (
    GetApiKeysRequestBody,
    GetApiKeysResponse,
    PostApiKeyRequest,
    PostApiKeyResponse,
)
from internal.deps.apikey import ApiKeyHandler, get_api_key_handler

router = APIRouter(prefix="/api-keys")


@router.post(
    "/all", response_model=GetApiKeysResponse, response_model_exclude_none=True
)
def all(body: GetApiKeysRequestBody, hdl: ApiKeyHandler = Depends(get_api_key_handler)):
    return hdl.all(body)


@router.post(
    "",
    response_model=PostApiKeyResponse,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True,
)
def create(
    request: PostApiKeyRequest, hdl: ApiKeyHandler = Depends(get_api_key_handler)
):
    return hdl.create(request)

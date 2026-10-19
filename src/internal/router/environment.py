from fastapi import APIRouter, Depends, status
from internal.dto.environment import (
    GetEnvironmentsRequestBody,
    GetEnvironmentsResponse,
    PostEnvironmentRequestBody,
    PostEnvironmentResponse,
)
from internal.deps.environment import EnvironmentHandler, get_environment_handler
from internal.deps.common import Claims, get_claims

router = APIRouter(prefix="/environments")


@router.post(
    "/all", response_model=GetEnvironmentsResponse, response_model_exclude_none=True
)
def all(
    body: GetEnvironmentsRequestBody,
    claims: Claims = Depends(get_claims),
    hdl: EnvironmentHandler = Depends(get_environment_handler),
):
    return hdl.all(body, claims)


@router.post(
    "",
    response_model=PostEnvironmentResponse,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True,
)
def create(
    body: PostEnvironmentRequestBody,
    claims: Claims = Depends(get_claims),
    hdl: EnvironmentHandler = Depends(get_environment_handler),
):
    return hdl.create(body, claims)

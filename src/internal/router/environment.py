from fastapi import APIRouter, Depends, status
from internal.dto.environment import (
    GetEnvironmentsRequestBody,
    GetEnvironmentsResponse,
    PostEnvironmentRequest,
    PostEnvironmentResponse,
)
from internal.deps.environment import EnvironmentHandler, get_environment_handler

router = APIRouter(prefix="/environments")


@router.post(
    "/all", response_model=GetEnvironmentsResponse, response_model_exclude_none=True
)
def all(
    body: GetEnvironmentsRequestBody,
    hdl: EnvironmentHandler = Depends(get_environment_handler),
):
    return hdl.all(body)


@router.post(
    "",
    response_model=PostEnvironmentResponse,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True,
)
def create(
    request: PostEnvironmentRequest,
    hdl: EnvironmentHandler = Depends(get_environment_handler),
):
    return hdl.create(request)

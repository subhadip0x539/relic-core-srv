from fastapi import APIRouter, Depends, status
from internal.dto.service import (
    GetServicesResponse,
    PostServiceRequest,
    PostServiceResponse,
    GetServicesRequestBody,
)
from internal.deps.service import ServiceHandler, get_service_handler

router = APIRouter(prefix="/services")


@router.post(
    "/all", response_model=GetServicesResponse, response_model_exclude_none=True
)
def all(
    body: GetServicesRequestBody, hdl: ServiceHandler = Depends(get_service_handler)
):
    return hdl.all(body)


@router.get(
    "/{service_id}",
    response_model=GetServicesResponse,
    response_model_exclude_none=True,
)
def get(service_id: str, hdl: ServiceHandler = Depends(get_service_handler)):
    return hdl.get(service_id)


@router.post(
    "",
    response_model=PostServiceResponse,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True,
)
def create(
    request: PostServiceRequest, hdl: ServiceHandler = Depends(get_service_handler)
):
    return hdl.create(request)

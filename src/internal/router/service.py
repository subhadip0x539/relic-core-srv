from fastapi import APIRouter, Depends, status
from internal.dto.service import (
    GetServicesResponse,
    PostServiceRequestBody,
    PostServiceResponse,
    GetServicesRequestBody,
)
from internal.deps.service import ServiceHandler, get_service_handler
from internal.deps.common import Claims, get_claims

router = APIRouter(prefix="/services")


@router.post(
    "/all", response_model=GetServicesResponse, response_model_exclude_none=True
)
def all(
    body: GetServicesRequestBody,
    claims: Claims = Depends(get_claims),
    hdl: ServiceHandler = Depends(get_service_handler),
):
    return hdl.all(body, claims)


@router.get(
    "/{service_id}",
    response_model=GetServicesResponse,
    response_model_exclude_none=True,
)
def get(
    service_id: str,
    claims: Claims = Depends(get_claims),
    hdl: ServiceHandler = Depends(get_service_handler),
):
    return hdl.get(service_id, claims)


@router.post(
    "",
    response_model=PostServiceResponse,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True,
)
def create(
    body: PostServiceRequestBody,
    claims: Claims = Depends(get_claims),
    hdl: ServiceHandler = Depends(get_service_handler),
):
    return hdl.create(body, claims)

from fastapi import APIRouter, Depends, status
from internal.dto.flag import (
    GetFlagsResponse,
    PostFlagRequestBody,
    PostFlagResponse,
    GetFlagsRequestBody,
    PatchFlagRequestBody,
    PatchFlagResponse,
)
from internal.deps.flag import FlagHandler, get_flag_handler
from internal.deps.common import Claims, get_claims

router = APIRouter(prefix="/flags")


@router.post("/all", response_model=GetFlagsResponse, response_model_exclude_none=True)
def all(
    body: GetFlagsRequestBody,
    claims: Claims = Depends(get_claims),
    hdl: FlagHandler = Depends(get_flag_handler),
):
    return hdl.all(body, claims)


@router.post(
    "",
    response_model=PostFlagResponse,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True,
)
def create(
    body: PostFlagRequestBody,
    claims: Claims = Depends(get_claims),
    hdl: FlagHandler = Depends(get_flag_handler),
):
    return hdl.create(body, claims)


@router.patch(
    "/{flag_id}",
    response_model=PatchFlagResponse,
    response_model_exclude_none=True,
)
async def update(
    flag_id: str,
    body: PatchFlagRequestBody,
    claims: Claims = Depends(get_claims),
    hdl: FlagHandler = Depends(get_flag_handler),
):
    return await hdl.update(flag_id, body, claims)

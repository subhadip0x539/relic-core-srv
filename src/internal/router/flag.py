from fastapi import APIRouter, Depends, status
from internal.dto.flag import (
    GetFlagsResponse,
    PostFlagRequest,
    PostFlagResponse,
    GetFlagsRequestBody,
    PatchFlagRequest,
    PatchFlagResponse,
)
from internal.deps.flag import FlagHandler, get_flag_handler

router = APIRouter(prefix="/flags")


@router.post("/all", response_model=GetFlagsResponse, response_model_exclude_none=True)
def all(body: GetFlagsRequestBody, hdl: FlagHandler = Depends(get_flag_handler)):
    return hdl.all(body)


@router.post(
    "",
    response_model=PostFlagResponse,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True,
)
def create(request: PostFlagRequest, hdl: FlagHandler = Depends(get_flag_handler)):
    return hdl.create(request)


@router.patch(
    "/{flag_id}",
    response_model=PatchFlagResponse,
    response_model_exclude_none=True,
)
async def update(
    flag_id: str,
    request: PatchFlagRequest,
    hdl: FlagHandler = Depends(get_flag_handler),
):
    return await hdl.update(flag_id, request)

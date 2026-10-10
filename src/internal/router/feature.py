from fastapi import APIRouter, Depends, Request
from internal.dto.feature import GetFeaturesResponse
from internal.deps.feature import FeatureHandler, get_feature_handler
from internal.deps.common import authorize

router = APIRouter(prefix="/features", dependencies=[Depends(authorize)])


@router.get("", response_model=GetFeaturesResponse, response_model_exclude_none=True)
def all(
    request: Request,
    hdl: FeatureHandler = Depends(get_feature_handler),
):
    return hdl.all(request.state.api_key)

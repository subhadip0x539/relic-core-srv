from fastapi import APIRouter, Depends
from internal.dto.feature import GetFeaturesResponse
from internal.deps.feature import FeatureHandler, get_feature_handler
from internal.deps.auth import get_api_key

router = APIRouter(prefix="/features")


@router.get("", response_model=GetFeaturesResponse, response_model_exclude_none=True)
def all(
    api_key: str = Depends(get_api_key),
    hdl: FeatureHandler = Depends(get_feature_handler),
):
    return hdl.all(api_key)

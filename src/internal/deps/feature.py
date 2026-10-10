from fastapi import Depends
from internal.services.feature import FeatureService
from internal.services.feature import FeatureServiceImpl
from internal.handlers.feature import FeatureHandler
from .apikey import ApiKeyRepository, get_api_key_repository
from .flag import FlagRepository, get_flag_repository


def get_feature_service(
    flag_repo: FlagRepository = Depends(get_flag_repository),
    api_key_repo: ApiKeyRepository = Depends(get_api_key_repository),
) -> FeatureService:
    return FeatureServiceImpl(flag_repo, api_key_repo)


def get_feature_handler(
    svc: FeatureService = Depends(get_feature_service),
) -> FeatureHandler:
    return FeatureHandler(svc)

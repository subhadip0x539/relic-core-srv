from .common import MongoClient, get_mongo_client
from fastapi import Depends
from internal.repositories.apikey import ApiKeyRepository, ApiKeyRepositoryImpl
from internal.services.apikey import ApiKeyService, ApiKeyServiceImpl
from .service import ServiceRepository, get_service_repository
from internal.handlers.apikey import ApiKeyHandler


def get_api_key_repository(
    mongo_client: MongoClient = Depends(get_mongo_client),
) -> ApiKeyRepository:
    return ApiKeyRepositoryImpl(mongo_client.db)


def get_api_key_service(
    api_key_repo: ApiKeyRepository = Depends(get_api_key_repository),
    service_repo: ServiceRepository = Depends(get_service_repository),
) -> ApiKeyService:
    return ApiKeyServiceImpl(api_key_repo, service_repo)


def get_api_key_handler(
    svc: ApiKeyService = Depends(get_api_key_service),
) -> ApiKeyHandler:
    return ApiKeyHandler(svc)

from internal.repositories.service import ServiceRepository, ServiceRepositoryImpl
from .common import MongoClient, get_mongo_client
from fastapi import Depends
from internal.services.service import ServiceService, ServiceServiceImpl
from internal.handlers.service import ServiceHandler


def get_service_repository(
    mongo_client: MongoClient = Depends(get_mongo_client),
) -> ServiceRepository:
    return ServiceRepositoryImpl(mongo_client.db)


def get_service_service(
    repo: ServiceRepository = Depends(get_service_repository),
) -> ServiceService:
    return ServiceServiceImpl(repo)


def get_service_handler(
    svc: ServiceService = Depends(get_service_service),
) -> ServiceHandler:
    return ServiceHandler(svc)

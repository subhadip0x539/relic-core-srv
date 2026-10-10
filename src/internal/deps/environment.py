from .common import MongoClient, get_mongo_client
from fastapi import Depends
from internal.repositories.environment import (
    EnvironmentRepository,
    EnvironmentRepositoryImpl,
)
from internal.services.environment import EnvironmentService, EnvironmentServiceImpl
from internal.handlers.environment import EnvironmentHandler


def get_environment_repository(
    mongo_client: MongoClient = Depends(get_mongo_client),
) -> EnvironmentRepository:
    return EnvironmentRepositoryImpl(mongo_client.db)


def get_environment_service(
    repo: EnvironmentRepository = Depends(get_environment_repository),
) -> EnvironmentService:
    return EnvironmentServiceImpl(repo)


def get_environment_handler(
    svc: EnvironmentService = Depends(get_environment_service),
) -> EnvironmentHandler:
    return EnvironmentHandler(svc)

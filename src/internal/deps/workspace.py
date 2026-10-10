from .common import MongoClient, get_mongo_client
from fastapi import Depends
from internal.repositories.workspace import WorkspaceRepository, WorkspaceRepositoryImpl
from internal.services.workspace import WorkspaceService, WorkspaceServiceImpl
from internal.handlers.workspace import WorkspaceHandler


def get_workspace_repository(
    mongo_client: MongoClient = Depends(get_mongo_client),
) -> WorkspaceRepository:
    return WorkspaceRepositoryImpl(mongo_client.db)


def get_workspace_service(
    repo: WorkspaceRepository = Depends(get_workspace_repository),
) -> WorkspaceService:
    return WorkspaceServiceImpl(repo)


def get_workspace_handler(
    svc: WorkspaceService = Depends(get_workspace_service),
) -> WorkspaceHandler:
    return WorkspaceHandler(svc)

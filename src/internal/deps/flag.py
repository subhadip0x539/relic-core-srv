from .common import MongoClient, get_mongo_client
from fastapi import Depends
from internal.repositories.flag import FlagRepository, FlagRepositoryImpl
from internal.services.flag import FlagService, FlagServiceImpl
from internal.handlers.flag import FlagHandler
from .common import EventManager, get_event_manager


def get_flag_repository(
    mongo_client: MongoClient = Depends(get_mongo_client),
    event_manager: EventManager = Depends(get_event_manager),
) -> FlagRepository:
    return FlagRepositoryImpl(mongo_client.db, event_manager)


def get_flag_service(
    repo: FlagRepository = Depends(get_flag_repository),
) -> FlagService:
    return FlagServiceImpl(repo)


def get_flag_handler(svc: FlagService = Depends(get_flag_service)) -> FlagHandler:
    return FlagHandler(svc)

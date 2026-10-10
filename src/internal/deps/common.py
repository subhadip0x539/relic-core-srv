from fastapi import Request, HTTPException, Header, status, Depends
from internal.infra.mongo import MongoClient
from typing import Optional
from config import config
from internal.lib.event import EventManager

mongo_client = (
    MongoClient()
    .uri(config.mongo.uri)
    .database_name(config.mongo.database_name)
    .connect()
)

event_manager = EventManager()


def get_mongo_client() -> MongoClient:
    return mongo_client


def authorize(
    request: Request,
    mongo_client: MongoClient = Depends(get_mongo_client),
    x_api_key: Optional[str] = Header(default=None, alias="X-API-Key"),
):
    api_key = x_api_key or request.path_params.get("api_key")

    if not api_key:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Unauthorized")

    db = mongo_client.db
    collection = db.get_collection("api_keys")

    doc = collection.find_one({"_id": api_key})

    if not doc:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Unauthorized")

    request.state.api_key = api_key

    service_id = doc["service_id"]

    request.state.service_id = service_id


def get_event_manager() -> EventManager:
    return event_manager

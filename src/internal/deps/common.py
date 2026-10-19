from internal.infra.mongo import MongoClient
from config import config
from internal.lib.event import EventManager
from typing import Annotated, Optional
from fastapi import Depends, HTTPException, status, Header
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from internal.domain.error import InvalidTokenError
from internal.lib.claims import Claims

bearer = HTTPBearer(auto_error=False)

mongo_client = (
    MongoClient()
    .uri(config.mongo.uri)
    .database_name(config.mongo.database_name)
    .connect()
)

event_manager = EventManager()


def get_mongo_client() -> MongoClient:
    return mongo_client


def get_event_manager() -> EventManager:
    return event_manager


def get_claims(
    creds: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer)],
) -> Claims:
    if not creds:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid token")
    try:
        return Claims(creds.credentials, config.auth.secret, config.auth.algorithm)
    except InvalidTokenError as exc:
        raise HTTPException(exc.code, exc.message)


def get_api_key(
    mongo_client: MongoClient = Depends(get_mongo_client),
    x_api_key: Optional[str] = Header(default=None, alias="X-API-Key"),
) -> str:
    if not x_api_key:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Unauthorized")

    collection = mongo_client.db.get_collection("api_keys")

    doc = collection.find_one({"_id": x_api_key})

    if not doc:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Unauthorized")

    return x_api_key

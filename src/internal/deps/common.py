from internal.infra.mongo import MongoClient
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


def get_event_manager() -> EventManager:
    return event_manager

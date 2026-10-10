from internal.port.flag import FlagRepository
from internal.domain.flag import Flag
from pymongo.database import Database
from typing import Any
from internal.lib.fc import FC
from internal.dto.flag import PatchFlagRequest
from internal.deps.common import EventManager


class FlagRepositoryImpl(FlagRepository):
    def __init__(self, db: Database[Any], em: EventManager):
        self._db = db
        self._em = em

    def all(self, fc: FC) -> list[Flag]:
        collection = self._db.get_collection("flags")

        docs = collection.find(fc.to_mongo_query())

        flags: list[Flag] = []

        for doc in docs:
            data = dict(doc)

            id = data.get("_id")

            if id is None:
                continue

            name = data.get("name", "")
            description = data.get("description", "")
            type = data.get("type", "")
            enabled = data.get("enabled", True)
            value = data.get("value", "")
            workspace_id = data.get("workspace_id", "")
            environment_id = data.get("environment_id", "")
            service_id = data.get("service_id", "")

            flags.append(
                Flag(
                    id=id,
                    name=name,
                    description=description,
                    type=type,
                    enabled=enabled,
                    value=value,
                    workspace_id=workspace_id,
                    environment_id=environment_id,
                    service_id=service_id,
                )
            )

        return flags

    def create(self, Flag: Flag) -> Flag:
        collection = self._db.get_collection("flags")

        collection.insert_one(
            {
                "_id": Flag.id,
                "name": Flag.name,
                "description": Flag.description,
                "type": Flag.type,
                "enabled": Flag.enabled,
                "value": Flag.value,
                "workspace_id": Flag.workspace_id,
                "environment_id": Flag.environment_id,
                "service_id": Flag.service_id,
            }
        )

        return Flag

    async def update(self, flag_id: str, payload: PatchFlagRequest):
        collection = self._db.get_collection("flags")

        fields = payload.model_dump(exclude_unset=True)

        if not fields:
            return

        collection.update_one(
            {"_id": flag_id},
            {"$set": fields},
        )

        flag = collection.find_one({"_id": flag_id})

        if not flag:
            return

        service_id = flag["service_id"]

        await self._em.notify(service_id, {"event": "flag.update", "flag_id": flag_id})

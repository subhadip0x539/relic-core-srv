from internal.port.apikey import ApiKeyRepository
from internal.domain.apikey import ApiKey
from pymongo.database import Database
from typing import Any
from internal.lib.fc import FC
from fastapi import HTTPException, status


class ApiKeyRepositoryImpl(ApiKeyRepository):
    def __init__(self, db: Database[Any]):
        self._db = db

    def all(self, fc: FC) -> list[ApiKey]:
        collection = self._db.get_collection("api_keys")

        docs = collection.find(fc.to_mongo_query())

        ApiKeys: list[ApiKey] = []

        for doc in docs:
            data = dict(doc)

            id = data.get("_id")

            if id is None:
                continue

            ApiKeys.append(
                ApiKey(
                    id=id,
                    workspace_id=data["workspace_id"],
                    environment_id=data["environment_id"],
                    service_id=data["service_id"],
                )
            )

        return ApiKeys

    def get(self, api_key: str) -> ApiKey:
        collection = self._db.get_collection("api_keys")

        doc = collection.find_one({"_id": api_key})

        if not doc:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Service not found",
            )

        return ApiKey(
            id=doc["_id"],
            workspace_id=doc["workspace_id"],
            environment_id=doc["environment_id"],
            service_id=doc["service_id"],
        )

    def create(self, api_key: ApiKey) -> ApiKey:
        collection = self._db.get_collection("api_keys")

        doc = collection.find_one({"service_id": api_key.service_id})

        if doc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"An API key for this service already exists",
            )

        collection.insert_one(
            {
                "_id": api_key.id,
                "workspace_id": api_key.workspace_id,
                "environment_id": api_key.environment_id,
                "service_id": api_key.service_id,
            }
        )

        return api_key

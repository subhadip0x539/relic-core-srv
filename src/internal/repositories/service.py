from internal.port.service import ServiceRepository
from internal.domain.service import Service
from pymongo.database import Database
from typing import Any
from internal.lib.fc import FC
from fastapi import HTTPException, status


class ServiceRepositoryImpl(ServiceRepository):
    def __init__(self, db: Database[Any]):
        self._db = db

    def all(self, fc: FC) -> list[Service]:
        collection = self._db.get_collection("services")

        docs = collection.find(fc.to_mongo_query())

        services: list[Service] = []

        for doc in docs:
            data = dict(doc)

            id = data.get("_id")

            if id is None:
                continue

            name = data.get("name", "")
            workspace_id = data.get("workspace_id", "")
            environment_id = data.get("environment_id", "")

            services.append(
                Service(
                    id=id,
                    workspace_id=workspace_id,
                    environment_id=environment_id,
                    name=name,
                )
            )

        return services

    def get(self, service_id: str) -> Service:
        collection = self._db.get_collection("services")

        doc = collection.find_one({"_id": service_id})

        if not doc:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Service not found",
            )

        return Service(
            id=doc["_id"],
            name=doc["name"],
            workspace_id=doc["workspace_id"],
            environment_id=doc["environment_id"],
        )

    def create(self, service: Service) -> Service:
        collection = self._db.get_collection("services")

        collection.insert_one(
            {
                "_id": service.id,
                "name": service.name,
                "workspace_id": service.workspace_id,
                "environment_id": service.environment_id,
            }
        )

        return service

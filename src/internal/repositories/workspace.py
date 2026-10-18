from internal.port.workspace import WorkspaceRepository
from internal.domain.workspace import Workspace
from pymongo.database import Database
from typing import Any
from datetime import datetime, timezone


class WorkspaceRepositoryImpl(WorkspaceRepository):
    def __init__(self, db: Database[Any]):
        self._db = db

    def all(self) -> list[Workspace]:
        collection = self._db.get_collection("workspaces")

        docs = collection.find()

        workspaces: list[Workspace] = []

        for doc in docs:
            workspaces.append(
                Workspace(
                    id=doc["_id"],
                    name=doc["name"],
                    created_at=doc["created_at"],
                    updated_at=doc["updated_at"],
                )
            )

        return workspaces

    def create(self, workspace: Workspace) -> Workspace:
        collection = self._db.get_collection("workspaces")

        now = datetime.now(timezone.utc)

        collection.insert_one(
            {
                "_id": workspace.id,
                "name": workspace.name,
                "created_at": now,
                "updated_at": now,
            }
        )

        return workspace

from internal.port.workspace import WorkspaceRepository
from internal.domain.workspace import Workspace
from pymongo.database import Database
from typing import Any

class WorkspaceRepositoryImpl(WorkspaceRepository):
    def __init__(self, db: Database[Any]):
        self._db = db

    def all(self) -> list[Workspace]:
        collection = self._db.get_collection("workspaces")

        docs = collection.find()

        workspaces: list[Workspace] = []

        for doc in docs:
            data = dict(doc)

            id = data.get("_id")

            if id is None:
                continue

            name = data.get("name", "")

            workspaces.append(Workspace(id=id, name=name))

        return workspaces
    
    def create(self, workspace: Workspace) -> Workspace:
        collection = self._db.get_collection("workspaces")

        collection.insert_one({
            "_id": workspace.id,
            "name": workspace.name,
        })

        return workspace
from internal.port.environment import EnvironmentRepository
from internal.domain.environment import Environment
from pymongo.database import Database
from typing import Any
from internal.lib.fc import FC


class EnvironmentRepositoryImpl(EnvironmentRepository):
    def __init__(self, db: Database[Any]):
        self._db = db

    def all(self, fc: FC) -> list[Environment]:
        collection = self._db.get_collection("environments")

        docs = collection.find(fc.to_mongo_query())

        environments: list[Environment] = []

        for doc in docs:
            data = dict(doc)

            id = data.get("_id")

            if id is None:
                continue

            name = data.get("name", "")
            color = data.get("color", "")
            workspace_id = data.get("workspace_id", "")

            environments.append(
                Environment(id=id, name=name, color=color, workspace_id=workspace_id)
            )

        return environments

    def create(self, environment: Environment) -> Environment:
        collection = self._db.get_collection("environments")

        collection.insert_one(
            {
                "_id": environment.id,
                "name": environment.name,
                "workspace_id": environment.workspace_id,
                "color": environment.color,
            }
        )

        return environment

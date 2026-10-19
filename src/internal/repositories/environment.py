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

            environments.append(
                Environment(
                    id=doc["_id"],
                    name=doc["name"],
                    color=doc["color"],
                    workspace_id=doc["workspace_id"],
                )
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

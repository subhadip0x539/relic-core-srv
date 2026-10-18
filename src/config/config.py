import os
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings
from typing import TypedDict

DEFAULT_MONGO_URI = "mongodb://user:P@ssw0Rd!@localhost:22017"
DEFAULT_MONGO_DATABASE_NAME = "relic_core"

DEFAULT_AUTH_SECRET = "secret"
DEFAULT_AUTH_ALGORITHM = "HS256"


class AuthData(TypedDict, total=False):
    secret: str
    algorithm: str


class ServerData(TypedDict, total=False):
    host: str
    port: int


class Server(BaseSettings):
    host: str = Field(default="localhost")
    port: int = Field(default=8080)


class MongoData(TypedDict, total=False):
    uri: str
    database_name: str


class Auth(BaseSettings):
    secret: str = Field(default=DEFAULT_AUTH_SECRET)
    algorithm: str = Field(default=DEFAULT_AUTH_ALGORITHM)


class Mongo(BaseSettings):
    uri: str = Field(default=DEFAULT_MONGO_URI)
    database_name: str = Field(default=DEFAULT_MONGO_DATABASE_NAME)


class Config(BaseSettings):
    server: Server = Field(default_factory=Server)
    mongo: Mongo = Field(default_factory=Mongo)
    auth: Auth = Field(default_factory=Auth)


class ConfigBuilder:

    def __init__(self):
        self._server_data: ServerData = {}
        self._mongo_data: MongoData = {}
        self._auth_data: AuthData = {}

    def env(self, file: str = ".env") -> "ConfigBuilder":
        load_dotenv(os.path.join(os.getcwd(), file))

        self._server_data.update(
            {
                "host": os.getenv("SERVER_HOST", "localhost"),
                "port": int(os.getenv("SERVER_PORT", 8000)),
            }
        )

        self._mongo_data.update(
            {
                "uri": os.getenv("MONGO_URI", DEFAULT_MONGO_URI),
                "database_name": os.getenv(
                    "MONGO_DATABASE", DEFAULT_MONGO_DATABASE_NAME
                ),
            }
        )

        self._auth_data.update(
            {
                "secret": os.getenv("AUTH_SECRET", DEFAULT_AUTH_SECRET),
                "algorithm": os.getenv("AUTH_ALGORITHM", DEFAULT_AUTH_ALGORITHM),
            }
        )

        return self

    def server(self, host: str = "localhost", port: int = 8000) -> "ConfigBuilder":
        self._server_data.update({"host": host, "port": port})
        return self

    def temporal(
        self, uri: str = DEFAULT_MONGO_URI, database: str = DEFAULT_MONGO_DATABASE_NAME
    ) -> "ConfigBuilder":
        self._mongo_data.update({"uri": uri, "database_name": database})
        return self

    def build(self) -> Config:
        return Config(
            server=Server(**self._server_data),
            mongo=Mongo(**self._mongo_data),
            auth=Auth(**self._auth_data),
        )

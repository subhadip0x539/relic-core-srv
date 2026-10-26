from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class Permission(str, Enum):
    WORKSPACE_READ = "workspace:read"
    WORKSPACE_CREATE = "workspace:create"
    WORKSPACE_UPDATE = "workspace:update"

    ENVIRONMENT_READ = "environment:read"
    ENVIRONMENT_CREATE = "environment:create"
    ENVIRONMENT_UPDATE = "environment:update"

    SERVICE_READ = "service:read"
    SERVICE_CREATE = "service:create"
    SERVICE_UPDATE = "service:update"

    FLAG_READ = "flag:read"
    FLAG_CREATE = "flag:create"
    FLAG_UPDATE = "flag:update"

    API_KEY_READ = "api_key:read"
    API_KEY_CREATE = "api_key:create"
    API_KEY_UPDATE = "api_key:update"


class Role(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    READONLY = "readonly"


class TokenClaims(BaseModel):
    sub: str
    role: Role
    permissions: list[Permission]
    jti: str
    iat: datetime
    exp: datetime

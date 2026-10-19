from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class Permission(str, Enum):
    WORKSPACE_READ = "workspace:read"
    WORKSPACE_CREATE = "workspace:create"

    ENVIRONMENT_READ = "environment:read"
    ENVIRONMENT_CREATE = "environment:create"

    SERVICE_CREATE = "service:create"

    FLAG_CREATE = "flag:create"


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

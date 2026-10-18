from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class Role(str, Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    MANAGER = "manager"
    VIEWER = "viewer"


class TokenClaims(BaseModel):
    sub: str
    roles: list[Role]
    jti: str
    iat: datetime
    exp: datetime

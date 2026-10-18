from pydantic import BaseModel
from datetime import datetime


class Workspace(BaseModel):
    id: str
    name: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

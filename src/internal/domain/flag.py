from pydantic import BaseModel
from typing import Optional


class Flag(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    type: str
    enabled: bool
    value: Optional[str | int | float] = None
    service_id: str
    environment_id: str
    workspace_id: str

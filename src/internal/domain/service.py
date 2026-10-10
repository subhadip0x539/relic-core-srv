from pydantic import BaseModel


class Service(BaseModel):
    id: str
    workspace_id: str
    environment_id: str
    name: str

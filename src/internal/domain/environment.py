from pydantic import BaseModel

class Environment(BaseModel):
    id: str
    name: str
    workspace_id: str
    color: str
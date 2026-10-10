from pydantic import BaseModel


class ApiKey(BaseModel):
    id: str
    workspace_id: str
    environment_id: str
    service_id: str

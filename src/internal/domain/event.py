from datetime import datetime
from pydantic import BaseModel, Field


class FlagUpdateEvent(BaseModel):
    event_type: str = "flag.updated"
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    flag_id: str
    service_id: str

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

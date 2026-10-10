from pydantic import BaseModel


class RequestBodyFilter(BaseModel):
    field: str
    operator: str
    value: list[str]


RequestBodyFilters = list[RequestBodyFilter]

from pydantic import BaseModel
from enum import Enum


class FilterOperator(str, Enum):
    EQ = "eq"
    IN = "in"
    NOT_IN = "nin"
    GT = "gt"
    LT = "lt"


class Filter(BaseModel):
    field: str
    operator: FilterOperator
    value: list[str]


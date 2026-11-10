from typing import Literal
from pydantic import BaseModel, Field

class HistoryItem(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(max_length=4000)

class AskIn(BaseModel):
    message: str = Field(min_length=1, max_length=500)
    history: list[HistoryItem] = Field(default_factory=list, max_length=10)

class AskOut(BaseModel):
    answer: str
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field


class ParagraphBlock(BaseModel):
    type: Literal["paragraph"]
    content: str

class HeadingBlock(BaseModel):
    type: Literal["heading"]
    content: str

class ListBlock(BaseModel):
    type: Literal["list"]
    items: list[str]

class QuoteBlock(BaseModel):
    type: Literal["quote"]
    content: str

Block = Annotated[
    Union[ParagraphBlock, HeadingBlock, ListBlock, QuoteBlock],
    Field(discriminator="type"),
]


class PostSummary(BaseModel):
    slug: str
    title: str
    date: str
    summary: str
    tags: list[str] = []
    readTime: str = ""      # camelCase on purpose, to match the JSON and the front end


class Post(PostSummary):
    body: list[Block]
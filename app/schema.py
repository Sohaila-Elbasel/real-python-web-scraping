from typing import List
from pydantic import BaseModel

class ArticleBase(BaseModel):
    id: int
    title: str
    url: str

    class Config:
        from_attributes = True

class ArticleIDBase(BaseModel):
    id: int

    class Config:
        from_attributes = True

class KeywordBase(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class KeywordSchema(KeywordBase):
    articles: List[ArticleIDBase]

class ArticleSchema(ArticleBase):
    keywords: List[KeywordBase]

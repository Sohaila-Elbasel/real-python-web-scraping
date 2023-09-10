from typing import List
from pydantic import BaseModel

class ArticleBase(BaseModel):
    id: int
    title: str
    url: str

    class ConfigDict:
        from_attributes = True

class ArticleIDBase(BaseModel):
    id: int

    class ConfigDict:
        from_attributes = True

class KeywordBase(BaseModel):
    id: int
    name: str

    class ConfigDict:
        from_attributes = True

class KeywordSchema(KeywordBase):
    articles: List[ArticleIDBase]

class ArticleSchema(ArticleBase):
    keywords: List[KeywordBase]

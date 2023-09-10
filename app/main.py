from typing import List
from fastapi import FastAPI
from app.schema import ArticleSchema, KeywordSchema

from scraper.scraping import update_data
from .models import Keyword, session, Article


app = FastAPI()

def get_application():
    _app = FastAPI()

    return _app

app = get_application()


@app.get("/", response_model=List[ArticleSchema])
def get_articles():    
    artilce_query = session.query(Article).all()
    return artilce_query
    

@app.get('/update')
def update():
    return update_data()

@app.get('/keywords', response_model=List[KeywordSchema])
def get_keywords():
    return session.query(Keyword).all()
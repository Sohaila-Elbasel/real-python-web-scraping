from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.ext.associationproxy import association_proxy
import os
from dotenv import load_dotenv

load_dotenv('.env')

url = os.environ['DATABASE_URL']

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

article_keywords = Table("article_keywords", Base.metadata,
                       Column("article_id", ForeignKey("article.id"), primary_key=True),
                       Column("keyword_id", ForeignKey("keyword.id"), primary_key=True))


class Keyword(Base):
    __tablename__= "keyword"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    articles = relationship("Article", secondary=article_keywords, back_populates="keywords")


class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    
    keywords = relationship("Keyword", secondary=article_keywords, back_populates="articles")

Base.metadata.create_all(engine)
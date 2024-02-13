from sqlalchemy.orm import Session
from database import DBArticle
from datetime import datetime

def get_article(db: Session, article_id: int):
    return db.query(DBArticle).filter(DBArticle.id == article_id).first()

def get_articles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DBArticle).offset(skip).limit(limit).all()

def create_article(db: Session, title: str, content: str, publish_date: datetime):
    db_article = DBArticle(title=title, content=content, publish_date=publish_date)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def update_article(db: Session, article: DBArticle, title: str, content: str, publish_date: datetime):
    article.title = title
    article.content = content
    article.publish_date = publish_date
    db.commit()
    db.refresh(article)
    return article

def delete_article(db: Session, article: DBArticle):
    db.delete(article)
    db.commit()

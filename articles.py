from datetime import datetime
from sqlalchemy.orm import Session
from database import DBArticle
from pydantic import BaseModel

# Modèle Pydantic pour la création d'un article
class ArticleCreate(BaseModel):
    title: str
    content: str
    publish_date: datetime

# Fonction pour obtenir un article par son ID
def get_article(db: Session, article_id: int):
    return db.query(DBArticle).filter(DBArticle.id == article_id).first()

# Fonction pour obtenir une liste d'articles avec pagination
def get_articles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DBArticle).offset(skip).limit(limit).all()

# Fonction pour créer un nouvel article
def create_article(db: Session, article: ArticleCreate):
    db_article = DBArticle(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

# Fonction pour mettre à jour un article existant
def update_article(db: Session, article_id: int, article_data: ArticleCreate):
    db_article = get_article(db, article_id)
    if db_article:
        for key, value in article_data.dict(exclude_unset=True).items():
            setattr(db_article, key, value)
        db.commit()
        db.refresh(db_article)
    return db_article

# Fonction pour supprimer un article
def delete_article(db: Session, article_id: int):
    db_article = get_article(db, article_id)
    if db_article:
        db.delete(db_article)
        db.commit()
    return db_article



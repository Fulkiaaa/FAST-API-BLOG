from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from datetime import datetime
import articles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuration CORS
origins = [
    "http://localhost",
    "http://localhost:3000",  # Application React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Créer les tables de la base de données
Base.metadata.create_all(bind=engine)

# Dépendance pour obtenir la session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/articles/")
def create_article(article: articles.ArticleCreate, db: Session = Depends(get_db)):
    return articles.create_article(db=db, article=article)

@app.get("/articles/")
def read_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return articles.get_articles(db=db, skip=skip, limit=limit)

@app.get("/articles/{article_id}")
def read_article(article_id: int, db: Session = Depends(get_db)):
    db_article = articles.get_article(db=db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article

@app.put("/articles/{article_id}")
def update_article(article_id: int, article: articles.ArticleCreate, db: Session = Depends(get_db)):
    db_article = articles.get_article(db=db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return articles.update_article(db=db, article_id=article_id, article_data=article)

@app.delete("/articles/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    db_article = articles.get_article(db=db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    articles.delete_article(db=db, article_id=article_id)
    return {"message": "Article deleted successfully"}

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import articles
from datetime import datetime

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency for getting the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/articles/")
def create_article(title: str, content: str, publish_date: datetime = datetime.utcnow(), db: Session = Depends(get_db)):
    return articles.create_article(db=db, title=title, content=content, publish_date=publish_date)

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
def update_article(article_id: int, title: str, content: str, publish_date: datetime, db: Session = Depends(get_db)):
    db_article = articles.get_article(db=db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return articles.update_article(db=db, article=db_article, title=title, content=content, publish_date=publish_date)

@app.delete("/articles/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    db_article = articles.get_article(db=db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    articles.delete_article(db=db, article=db_article)
    return {"message": "Article deleted successfully"}

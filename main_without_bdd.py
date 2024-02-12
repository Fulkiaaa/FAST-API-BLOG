from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI()

class Article(BaseModel):
    id: int
    title: str
    content: str
    publication_date: datetime

# Exemple de données initiales
articles = [
    Article(id=1, title="Premier article", content="Contenu du premier article", publication_date=datetime.now()),
    Article(id=2, title="Deuxième article", content="Contenu du deuxième article", publication_date=datetime.now())
]

@app.get("/articles/", response_model=List[Article])
async def read_articles():
    return articles

@app.get("/articles/{article_id}", response_model=Article)
async def read_article(article_id: int):
    for article in articles:
        if article.id == article_id:
            return article
    raise HTTPException(status_code=404, detail="Article non trouvé")

@app.post("/articles/")
async def create_article(article: Article):
    articles.append(article)
    return {"message": "Article créé avec succès"}

@app.put("/articles/{article_id}")
async def update_article(article_id: int, updated_article: Article):
    for index, article in enumerate(articles):
        if article.id == article_id:
            articles[index] = updated_article
            return {"message": "Article mis à jour avec succès"}
    raise HTTPException(status_code=404, detail="Article non trouvé")

@app.delete("/articles/{article_id}")
async def delete_article(article_id: int):
    for index, article in enumerate(articles):
        if article.id == article_id:
            del articles[index]
            return {"message": "Article supprimé avec succès"}
    raise HTTPException(status_code=404, detail="Article non trouvé")

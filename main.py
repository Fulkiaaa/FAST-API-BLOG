from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models.article import Article
from typing import List
from database.database import create_article, read_articles, read_article, update_article, delete_article

app = FastAPI()

security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "user"
    correct_password = "1234"
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True

@app.get("/secure_endpoint/")
async def secure_endpoint(authenticated: bool = Depends(authenticate)):
    return {"message": "This is a secure endpoint"}

#FILTRAGE
@app.get("/articles/", response_model=List[Article])
async def get_articles(title: str = None):
    articles = read_articles()
    if title:
        articles = [article for article in articles if title.lower() in article.title.lower()]
    return articles

#PAGINATION
@app.get("/articles/", response_model=List[Article])
async def get_articles(skip: int = 0, limit: int = 10):
    articles = read_articles()
    return articles[skip:skip + limit]

#RECHERCHE
@app.get("/articles/", response_model=List[Article])
async def get_articles(query: str = None):
    articles = read_articles()
    if query:
        articles = [article for article in articles if query.lower() in article.title.lower() or query.lower() in article.content.lower()]
    return articles

#GET ALL
@app.get("/articles/", response_model=list[Article])
async def get_articles():
    return read_articles()

#GET ONE
@app.get("/articles/{article_id}", response_model=Article)
async def get_article(article_id: int):
    return read_article(article_id)

#POST ONE
@app.post("/articles/", response_model=Article)
async def create_new_article(article: Article):
    return create_article(article)

#EDIT ONE
@app.put("/articles/{article_id}", response_model=Article)
async def update_existing_article(article_id: int, article: Article):
    return update_article(article_id, article)

#DELETE ONE
@app.delete("/articles/{article_id}", response_model=Article)
async def delete_existing_article(article_id: int):
    return delete_article(article_id)

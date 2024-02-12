from pydantic import BaseModel
from datetime import datetime

class Article(BaseModel):
    id: int
    title: str
    content: str
    publication_date: datetime

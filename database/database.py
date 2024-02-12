import sqlite3
from models.article import Article

DATABASE_FILE = "blog.db"

def create_connection():
    conn = sqlite3.connect(DATABASE_FILE)
    return conn

def create_tables():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS articles
                 (id INTEGER PRIMARY KEY, title TEXT, content TEXT, publication_date TIMESTAMP)''')
    conn.commit()
    conn.close()
create_tables()

def create_article(article: Article):
    conn = create_connection()
    c = conn.cursor()
    c.execute('''INSERT INTO articles (id, title, content, publication_date) 
                 VALUES (?, ?, ?, ?)''', (article.id, article.title, article.content, article.publication_date))
    conn.commit()
    conn.close()
    return article

def read_articles():
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT id, title, content, publication_date FROM articles")
    articles = [Article(id=row[0], title=row[1], content=row[2], publication_date=row[3]) for row in c.fetchall()]
    conn.close()
    return articles

def read_article(article_id: int):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT id, title, content, publication_date FROM articles WHERE id=?", (article_id,))
    row = c.fetchone()
    if row:
        return Article(id=row[0], title=row[1], content=row[2], publication_date=row[3])
    return None

def update_article(article_id: int, updated_article: Article):
    conn = create_connection()
    c = conn.cursor()
    c.execute('''UPDATE articles 
                 SET title=?, content=?, publication_date=? 
                 WHERE id=?''', (updated_article.title, updated_article.content, 
                                 updated_article.publication_date, article_id))
    conn.commit()
    conn.close()
    return updated_article

def delete_article(article_id: int):
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM articles WHERE id=?", (article_id,))
    conn.commit()
    conn.close()
    return {"message": "Article deleted successfully"}
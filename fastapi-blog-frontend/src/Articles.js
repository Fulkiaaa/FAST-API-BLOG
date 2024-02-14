import React, { useState, useEffect } from "react";
import axios from "axios";

function Articles() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchArticles() {
      try {
        const response = await axios.get("http://localhost:8000/articles/");
        setArticles(response.data.reverse());
        setLoading(false);
      } catch (error) {
        console.error("Error fetching articles:", error);
      }
    }

    fetchArticles();
  }, []);

  const handleDeleteArticle = async (articleId) => {
    try {
      await axios.delete(`http://localhost:8000/articles/${articleId}`);
      alert("Article supprimé avec succès !");
      window.location.reload();
    } catch (error) {
      console.error("Error deleting article:", error);
      alert("Une erreur s'est produite lors de la suppression de l'article.");
    }
  };

  if (loading) {
    return <div>Loading articles...</div>;
  }

  return (
    <div>
      <h2>Articles</h2>
      <ul>
        {articles.map((article) => (
          <div
            key={article.id}
            style={{
              display: "flex",
              justifyContent: "space-between",
              borderBottom: "1px solid #ccc",
              marginBottom: "10px",
              paddingBottom: "10px",
            }}
          >
            <div>
              <h3>{article.title}</h3>
              <p>{article.content}</p>
            </div>
            <div>
              <button
                class="btn-delete"
                onClick={() => handleDeleteArticle(article.id)}
              >
                Supprimer
              </button>
            </div>
          </div>
        ))}
      </ul>
    </div>
  );
}

export default Articles;

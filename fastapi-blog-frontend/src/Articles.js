import React, { useState, useEffect } from "react";
import axios from "axios";

function Articles() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [editingArticle, setEditingArticle] = useState(null);
  const [editTitle, setEditTitle] = useState("");
  const [editContent, setEditContent] = useState("");

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

  const handleEditArticle = (article) => {
    setEditingArticle(article);
    setEditTitle(article.title);
    setEditContent(article.content);
    console.log("article", article);
  };

  const handleSubmitEdit = async (e) => {
    e.preventDefault();
    // console.log("e", e);
    try {
      await axios.put(`http://localhost:8000/articles/${editingArticle.id}`, {
        title: editTitle,
        content: editContent,
      });
      alert("Article mis à jour avec succès !");
      setEditingArticle(null);
      window.location.reload();
    } catch (error) {
      console.error("Error updating article:", error);
      alert("Une erreur s'est produite lors de la mise à jour de l'article.");
    }
  };

  return (
    <div>
      <h2>Liste des articles</h2>
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
              <button onClick={() => handleEditArticle(article)}>
                Modifier
              </button>
              <button
                className="btn-delete"
                onClick={() => handleDeleteArticle(article.id)}
              >
                Supprimer
              </button>
            </div>
          </div>
        ))}
      </ul>
      {editingArticle && (
        <div>
          <h2>Modifier l'article</h2>
          <form onSubmit={handleSubmitEdit}>
            <div>
              <label htmlFor="editTitle">Titre :</label>
              <input
                type="text"
                id="editTitle"
                value={editTitle}
                onChange={(e) => setEditTitle(e.target.value)}
                required
              />
            </div>
            <div>
              <label htmlFor="editContent">Contenu :</label>
              <textarea
                id="editContent"
                value={editContent}
                onChange={(e) => setEditContent(e.target.value)}
                required
              />
            </div>
            <button type="submit">Enregistrer les modifications</button>
            <button onClick={() => setEditingArticle(null)}>Annuler</button>
          </form>
        </div>
      )}
    </div>
  );
}

export default Articles;

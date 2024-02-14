import React, { useState } from "react";
import axios from "axios";

function AddArticleForm() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:8000/articles/", {
        title: title,
        content: content,
        publish_date: new Date().toISOString(), // Ajoutez la date de publication actuelle
      });
      // Réinitialiser le formulaire après l'ajout d'un article
      setTitle("");
      setContent("");
      alert("Article ajouté avec succès !");
      window.location.reload();
    } catch (error) {
      console.error("Error adding article:", error);
      alert("Une erreur s'est produite lors de l'ajout de l'article.");
    }
  };

  return (
    <div>
      <h2>Ajouter un nouvel article</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="title">Titre :</label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="content">Contenu :</label>
          <textarea
            id="content"
            value={content}
            onChange={(e) => setContent(e.target.value)}
            required
          />
        </div>
        <button type="submit">Ajouter</button>
      </form>
    </div>
  );
}

export default AddArticleForm;

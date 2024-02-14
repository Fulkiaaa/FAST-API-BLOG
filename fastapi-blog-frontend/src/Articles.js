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

  if (loading) {
    return <div>Loading articles...</div>;
  }

  return (
    <div>
      <h2>Articles</h2>
      <ul>
        {articles.map((article) => (
          <ul key={article.id}>
            <h3>{article.title}</h3>
            <p>{article.content}</p>
            <hr />
          </ul>
        ))}
      </ul>
    </div>
  );
}

export default Articles;

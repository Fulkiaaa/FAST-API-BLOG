import React from "react";
import Articles from "./Articles";
import AddArticleForm from "./AddArticleForm";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Articles App</h1>
      </header>
      <AddArticleForm />
      <Articles />
    </div>
  );
}

export default App;

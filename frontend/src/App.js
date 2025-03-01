import React from "react";
import "./App.css";  

function App() {
  return (
    <div 
      className="app-container" 
      style={{ 
        /* backgroundImage: `url(${process.env.PUBLIC_URL + "/background.jpg"})`, */
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundAttachment: "fixed",
        display: "flex",
        flexDirection: "column",
      }}
    >
      <h1 className="main-title">Speech Emotion Recognition</h1>
      
      <div className="section">
        <h2>Real-Time Analysis</h2>
      </div>

      <div className="section">
        <h2>Upload Audio File</h2>
      </div>
    </div>
  );
}

export default App;

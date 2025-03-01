import React, { useState } from "react";

const Upload = ({ setEmotion }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const analyzeEmotion = async () => {
    if (!selectedFile) return;

    const formData = new FormData();
    formData.append("file", selectedFile);

    const response = await fetch("http://localhost:5000/analyze", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();
    setEmotion(result.emotion);
  };

  return (
    <div className="upload-container">
      <h2>📂 Upload an Audio File</h2>
      <input type="file" accept="audio/*" onChange={handleFileChange} />
      {selectedFile && <button onClick={analyzeEmotion}>Analyze Emotion</button>}
    </div>
  );
};

export default Upload;

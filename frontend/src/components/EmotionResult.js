import React from "react";

const EmotionResult = ({ emotion }) => {
  return (
    <div className="emotion-result">
      <h2>🔍 Emotion Analysis Result</h2>
      <p>Your detected emotion: <strong>{emotion}</strong></p>
    </div>
  );
};

export default EmotionResult;

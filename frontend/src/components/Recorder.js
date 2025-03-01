import React, { useState, useRef } from "react";

const Recorder = ({ setEmotion }) => {
  const [isRecording, setIsRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState(null);
  const mediaRecorder = useRef(null);
  const audioChunks = useRef([]);

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder.current = new MediaRecorder(stream);
    
    mediaRecorder.current.ondataavailable = (event) => {
      audioChunks.current.push(event.data);
    };

    mediaRecorder.current.onstop = () => {
      const audioBlob = new Blob(audioChunks.current, { type: "audio/wav" });
      setAudioBlob(audioBlob);
      audioChunks.current = [];
    };

    mediaRecorder.current.start();
    setIsRecording(true);
  };

  const stopRecording = () => {
    mediaRecorder.current.stop();
    setIsRecording(false);
  };

  const analyzeEmotion = async () => {
    if (!audioBlob) return;
    
    const formData = new FormData();
    formData.append("file", audioBlob, "recorded_audio.wav");
    
    const response = await fetch("http://localhost:5000/analyze", {
      method: "POST",
      body: formData,
    });
    
    const result = await response.json();
    setEmotion(result.emotion);
  };

  return (
    <div className="recorder-container">
      <h2>🎤 Record Your Speech</h2>
      <button onClick={startRecording} disabled={isRecording}>Start Recording</button>
      <button onClick={stopRecording} disabled={!isRecording}>Stop Recording</button>
      {audioBlob && <button onClick={analyzeEmotion}>Analyze Emotion</button>}
    </div>
  );
};

export default Recorder;

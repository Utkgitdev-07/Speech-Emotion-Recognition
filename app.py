from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import librosa
import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wav
import tensorflow as tf
import json
import os
import threading
import time
from datetime import datetime
from utils.preprocess import extract_features
from utils.predict import predict_emotion

app = Flask(__name__, static_folder="frontend/build", static_url_path="/")
CORS(app)  # Allow frontend to access backend

# Load trained model
model = tf.keras.models.load_model("model/trained_model.h5")

# Load emotion labels
with open("model/class_labels.json", "r") as f:
    class_labels = json.load(f)

recording = False  # Flag to control recording
audio_data = []  # Store recorded chunks
sr = 22050  # Sampling rate

def record_audio():
    """ Continuously records audio until stopped """
    global recording, audio_data
    audio_data = []  # Reset audio data
    print("🎙️ Recording started... Speak now.")

    while recording:
        audio_chunk = sd.rec(int(sr * 0.5), samplerate=sr, channels=1, dtype=np.int16)
        sd.wait()
        audio_data.append(audio_chunk)

    print("🛑 Recording stopped.")
    
    if audio_data:
        audio_array = np.concatenate(audio_data, axis=0)

        # Ensure recordings folder exists
        os.makedirs("recordings", exist_ok=True)

        # Save with a unique filename (timestamp)
        filename = f"recordings/recorded_audio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        wav.write(filename, sr, audio_array)

        return filename
    return None

@app.route("/")
def serve():
    return send_from_directory("frontend/build", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("frontend/build", path)

@app.route("/start", methods=["POST"])
def start_recording():
    """ Start recording audio """
    global recording
    if not recording:
        recording = True
        threading.Thread(target=record_audio, daemon=True).start()
        return jsonify({"status": "Recording started. Speak now!"})
    return jsonify({"status": "Already recording."})

@app.route("/stop", methods=["POST"])
def stop_recording():
    """ Stop recording and analyze the emotion """
    global recording
    if recording:
        recording = False
        time.sleep(1)  # Allow time for recording thread to stop

        # Ensure recordings folder exists before listing files
        if not os.path.exists("recordings"):
            return jsonify({"error": "No recordings found."}), 400

        files = sorted(os.listdir("recordings"), reverse=True)
        if not files:
            return jsonify({"error": "No recordings found."}), 400

        latest_file = files[0]
        file_path = os.path.join("recordings", latest_file)

        # Extract features and predict
        features = extract_features(file_path)
        emotion = predict_emotion(features, model, class_labels)

        return jsonify({"status": "Recording saved successfully!", "file": latest_file, "emotion": emotion})

    return jsonify({"status": "No active recording."})

@app.route("/upload", methods=["POST"])
def upload_file():
    """ Upload an audio file and predict emotion """
    if "audioFile" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["audioFile"]
    
    # Ensure uploaded recordings folder exists
    os.makedirs("uploaded_recordings", exist_ok=True)

    file_path = os.path.join("uploaded_recordings", file.filename)
    file.save(file_path)

    # Extract features and predict
    features = extract_features(file_path)
    emotion = predict_emotion(features, model, class_labels)

    return jsonify({"status": "File uploaded successfully!", "file": file.filename, "emotion": emotion})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)


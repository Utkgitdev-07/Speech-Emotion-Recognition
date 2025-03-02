# Speech Emotion Recognition

## 📌 Project Overview
This project is a **Speech Emotion Recognition** system that processes audio recordings to classify emotions. It utilizes deep learning techniques trained on the **TESS (Toronto Emotional Speech Set) dataset** and provides real-time analysis for both **recorded and uploaded audio files**.

## 📂 Folder Structure
```
Speech_Emotion_Recognition/
│── dataset/                     # Store audio files for training  
│   ├── TESS/                    # Contains the TESS dataset  
│── models/                       # Trained model & class labels  
│   ├── trained_model.h5          # Pre-trained emotion recognition model  
│   ├── class_labels.json         # Mapping of class labels  
│── utils/                        # Helper scripts  
│   ├── preprocess.py             # Feature extraction functions  
│   ├── predict.py                # Prediction logic  
│── notebooks/                    # Jupyter notebooks  
│   ├── Speech_emotion_recognition_project.ipynb  # Model training/testing notebook  
│── env/                          # Python virtual environment  
│── recordings/                   # Stores recorded audio files  
│── uploaded_recordings/          # Stores uploaded audio files  
│── app.py                        # Main Flask application  
│── requirements.txt              # Python dependencies  
│── frontend/                     # React Frontend  
│   ├── public/                    # Static assets (index.html, icons, etc.)  
│   ├── src/                       # React source code  
│   │   ├── components/            # React components  
│   │   ├── App.js                 # Main React component  
│   │   ├── index.js               # Entry point for React app  
│   │   ├── App.css                # Global styles  
│   ├── package.json               # React dependencies & scripts  
│── README.md                      # Project documentation  
```

## 🛠️ Tech Stack
### **Backend**
- Python
- Flask
- TensorFlow/Keras (for deep learning model)
- Librosa (for audio feature extraction)

### **Frontend**
- React.js
- HTML/CSS
- JavaScript

## 🔹 Features
✅ **Real-time Emotion Detection** – Supports live recordings and file uploads  
✅ **Deep Learning-Based Prediction** – Uses a pre-trained model on the TESS dataset  
✅ **Interactive Frontend** – User-friendly interface for recording and uploading files  
✅ **Flask API** – Backend for processing and predicting emotions from audio files  

## 🚀 How to Run the Project
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Utkgitdev-07/Speech-Emotion-Recognition.git
cd Speech-Emotion-Recognition
```

### 2️⃣ Install Dependencies
#### 🔹 Backend

**Create a Virtual Environment:**

Open your terminal/command prompt and navigate to the project folder. Then, create and activate a virtual environment:
```sh
python -m venv venv      # Create a virtual environment
source venv/bin/activate # For macOS/Linux
venv\Scripts\activate    # For Windows
```
Install Requirements
```sh
pip install -r requirements.txt
```

#### 🔹 Frontend
```sh
cd frontend
npm install
```

### 3️⃣ Build and Run the Application
#### 🔹 Build Frontend
Run the following command inside the frontend directory to create a production-ready build
```sh
cd frontend
npm run build
```
This will generate a build/ folder inside frontend/.

#### 🔹 Start Backend Server
Navigate to the project root and run:
```sh
python app.py
```
This will start the Flask server, which serves the React frontend and provides the API for emotion detection.

#### 🔹 Access the Application

Once the Flask server is running, open your browser and visit:
```sh
http://127.0.0.1:5000
```
The frontend will be available, allowing you to record/upload audio and get emotion predictions.

## 📊 Dataset Information
- **Dataset Name**: Toronto Emotional Speech Set (TESS)
- **Total Samples**: ~2,800 recordings
- **Emotions Covered**:
  - Angry
  - Disgust
  - Fear
  - Happy
  - Neutral
  - Pleasant Surprise
  - Sad
 
## Notes

 - Ensure you have Python and Node.js installed.

 - The trained model (trained_model.h5) should be placed in the models/ directory.

 - Flask automatically serves the built frontend from frontend/build/.

## 📩 Contributing
If you'd like to contribute to this project, feel free to fork the repository, create a feature branch, and submit a pull request! 😊

## 📜 License
This project is licensed under the **MIT License**.

---
Made with ❤️ by [Utkarsh Yadav](https://github.com/Utkgitdev-07) 🚀


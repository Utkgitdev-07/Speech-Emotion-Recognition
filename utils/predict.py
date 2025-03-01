import numpy as np

def predict_emotion(features, model, class_labels):
    """
    Predicts the emotion from extracted features using the trained model.

    Args:
        features (numpy.ndarray): Extracted audio features.
        model (tensorflow Model): Trained emotion classification model.
        class_labels (dict): Mapping of class indices to emotion labels.

    Returns:
        str: Predicted emotion label.
    """
    # Ensure features are in correct shape for prediction
    features = np.array(features, dtype=np.float32)
    
    # Make prediction
    prediction = model.predict(features)
    
    # Get the class with the highest probability
    predicted_class = np.argmax(prediction)
    
    # Return the corresponding emotion label
    return class_labels.get(str(predicted_class), "Unknown")

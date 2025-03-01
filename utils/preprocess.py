import librosa
import numpy as np

def extract_features(file_path):
    """
    Extracts MFCC features from an audio file.

    Args:
        file_path (str): Path to the audio file.

    Returns:
        numpy.ndarray: Extracted MFCC features reshaped for model input.
    """
    try:
        # Load the audio file
        audio, sr = librosa.load(file_path, sr=22050)

        # Extract MFCC features
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)

        # Compute the mean across time axis
        mfccs = np.mean(mfccs.T, axis=0)

        # Ensure correct shape for model input
        return np.expand_dims(mfccs, axis=0)

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return None

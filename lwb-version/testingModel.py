import pickle
from pathlib import Path

MODEL_DIR = Path(__file__).parent / "Model"

# Load the trained model
with open(MODEL_DIR / "spam_detector_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load the TF-IDF vectorizer
with open(MODEL_DIR / "tf_vectorizer2.pkl", "rb") as file:
    tf = pickle.load(file)


def getMessageType(uploadedtext):
    text_vectorized = tf.transform([uploadedtext])
    prediction = model.predict(text_vectorized)[0]
    return prediction

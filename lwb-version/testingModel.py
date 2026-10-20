import pickle
from pathlib import Path

MODEL_DIR = Path(__file__).parent / "Model"

# Load the trained model
with open(MODEL_DIR / "spam_detector_model.pkl", "rb") as file: #change to Correct_spam_detector_model.pkl
    model = pickle.load(file)

# Load the TF-IDF vectorizer
with open(MODEL_DIR / "tf_vectorizer2.pkl", "rb") as file: #change to Correct_tf_vectorizer.pkl
    tf = pickle.load(file)


def getMessageType(uploadedtext):
    text_vectorized = tf.transform([uploadedtext])
    prediction = model.predict(text_vectorized)[0]


    #confidences= model.predict_proba(text_vectorized)[0]
    #predicted_index = list(model.classes_).index(prediction)
    #confidence = confidences[predicted_index] * 100
    #Note: Make sure you rounded off the number. Ex. roundConfidence = round(confidence, 2)
    return prediction #, confidence




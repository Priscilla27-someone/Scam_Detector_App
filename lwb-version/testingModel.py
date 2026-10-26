from pathlib import Path
import pickle

# Load the trained model
with open("Model/spam_detector_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load the TF-IDF vectorizer
with open("Model/tf_vectorizer2.pkl", "rb") as file:
    tf = pickle.load(file)

def getprediction(text): 
    text_vectorized = tf.transform([text])
    prediction = model.predict(text_vectorized)[0]
    return prediction

def getconfidence(text):
    text_vectorized = tf.transform([text])
    prediction = model.predict(text_vectorized)[0]
    confidences = model.predict_proba(text_vectorized)[0]
    predicted_index = list(model.classes_).index(prediction)
    confidence = confidences[predicted_index] * 100
    return confidence




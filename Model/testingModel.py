
import pickle

# Load the trained model
with open("Model/spam_detector_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load the TF-IDF vectorizer
with open("Model/tf_vectorizer2.pkl", "rb") as file:
    tf = pickle.load(file)

# Ask the user for an email or text message
text = input("Paste the email or message you want to check:\n")

# Convert the text into numerical features
text_vectorized = tf.transform([text])

# Predict the category
prediction = model.predict(text_vectorized)[0]

# Display the result
if prediction == 0:
    print("\nResult: This is mostly a legimate message! No need to worry. (Ham)")
elif prediction == 1:
    print("\nResult: They are probably trying to steal your information! (Smishing, possible phishing scam)")
elif prediction == 2:
    print("\nResult: They are probably trying the scam you!!! (Spam, possible spam)")
else:
    print("\nUnknown category:", prediction)
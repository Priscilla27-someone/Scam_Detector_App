
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
# Note: Im using the Random Forest model. It's still under the same file name.
text_vectorized = tf.transform([text])

# Predict the category and confidence level
prediction = model.predict(text_vectorized)[0]
confidences= model.predict_proba(text_vectorized)[0] #Not every model type can use predict_proba

#Confidence precentage
predicted_index = list(model.classes_).index(prediction)
confidence = confidences[predicted_index] * 100

# Display the result
if prediction == 0:
    print(f"\nResult: This is mostly a legimate message! No need to worry. I am {confidence:.2f}%" , "confident")
    
elif prediction == 1:
    print("\nResult: They are probably trying to steal your information! (Smishing, possible phishing scam) I am {confidence:.2f}%" , "confident")
elif prediction == 2:
    print("\nResult: They are probably trying the scam you!!! (Spam, possible spam) I am {confidence:.2f}%" , "confident")
else:
    print("\nUnknown category:", prediction)

print(f"\nConfidence: {confidence:.4f}%")


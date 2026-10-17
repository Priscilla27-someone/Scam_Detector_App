import streamlit as st
import pytesseract as pt
pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image, ImageOps
from testingModel import getMessageType

col1, col2 = st.columns([3, 2])

with col1:
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="Uploaded Image", use_container_width=True)

with col2:
    if uploaded_file is not None:
        text = pt.image_to_string(img)
        prediction = getMessageType(text)
        if prediction == 1:
            predictiontype = ":red[Scam]"
        elif prediction == 2:
            predictiontype = ":yellow[Spam]"
        else:
            predictiontype = ":green[Likely Clean]"
        
        st.write("Detected text: ", text)
        st.write("Prediction: ", predictiontype)

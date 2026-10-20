import streamlit as st
import pytesseract as pt
pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image, ImageOps
from testingModel import getMessageType

st.set_page_config(
    page_title="Scam/Spam Checker",
    layout="wide"
)

col1, col2 = st.columns([1, 3])

def prediction(text, wantsPrediction, wantsString):
    prediction = getMessageType(text)
    if wantsPrediction: 
        if prediction == 1:
            predictiontype = ":red[Scam]"
        elif prediction == 2:
            predictiontype = ":yellow[Spam]"
        else:
            predictiontype = ":green[Safe]"
        return predictiontype
    elif wantsString:
        if prediction == 1:
            predictionStringtype = ("#### Please utilize extreme caution before interacting with this message. There is a high probability that it may be a threat actor trying to compromise your information.")
        elif prediction == 2:
            predictionStringtype = ("#### Please utilize caution before interacting.")
        else:
            predictionStringtype = ("#### While this message is believably safe, our prediction model may incorrectly guess some texts. Please still utilize caution at your discretion before interacting.")
        return predictionStringtype
    else:
        return prediction


with col1:
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])
    uploaded_text = st.text_input("Input a message...", placeholder='type here')
    if uploaded_file is not None:
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="Uploaded Image", use_container_width=True)

with col2:
    if uploaded_text.strip():
        text = uploaded_text
        st.write("# This is likely a " + prediction(text, True, False) + " text.")

    if uploaded_file is not None:
        text = pt.image_to_string(img)
        st.write("# This is likely a " + prediction(text, True, False) + " text.")
        st.write(prediction(text, False, True))
        


        with st.container(border=True):
            st.write("### Detected text: ")
            st.write(text)




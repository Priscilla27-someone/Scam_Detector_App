import streamlit as st
import pytesseract as pt
from testingModel import getprediction
from testingModel import getconfidence
from PIL import Image, ImageOps
from streamlit_echarts import st_echarts
import io
import textwrap

pt.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"

st.set_page_config(
    page_title="Scamurai",
    layout="wide"
)
page_bg_img = """
<style>
.stApp {background-color: #E5E5F7;
background: 
radial-gradient(#1c1c1c 15%, transparent 1%) 0 0, 
radial-gradient(#1c1c1c 15%, transparent 1%) 5px 5px, 
radial-gradient(#1c1c1c 15%, transparent 1%) 0 1px, 
radial-gradient(#1c1c1c 15%, transparent 1%) 5px 6px;
background-size: 10px 10px;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

if "image_bytes" not in st.session_state:
    st.session_state.image_bytes = None

if "uploaded_text" not in st.session_state:
    st.session_state.uploaded_text = None

def useImageLayout():
    image = Image.open(io.BytesIO(st.session_state.image_bytes)) 
    predictionNumber = getType(image)
    st.title(":red[Scam]urai", text_alignment='center', icon="⚔️")
    col1, col2 = st.columns([3, 1])
    with col2:
        st_echarts(options=getOptions(predictionNumber, grabConfidence(image)), height='200px', width='200px')
    with col1:
        st.space(size="small")
        st.space(size="xxsmall")
        st.title(getText(predictionNumber), text_alignment="center")

    col2, col3 = st.columns([2, 2])
    with col2:
        st.image(image)
    with col3:
        st.subheader("Recommended Next Steps", text_alignment='center')
        with st.container(border=True):
            if predictionNumber == 0:
                st.write("1. We are pretty sure this is a :green[safe message!] However, our prediction model can be wrong. Please interact with it at your discretion.")
                st.divider()
                st.write("2. Remember, don't give :green[any sensitive info] that a complete stranger would need because it could always be a bad actor trying to get your information.")
            elif predictionNumber == 1:
                st.write("1. If you have already clicked a link or given information, please :red[disconnect your device from the internet] as soon as possible and :red[run a malware scan] for hidden threats. If you entered passwords or login details, :red[immediately change that information] on those platforms. If you shared financial information, :red[call your bank or credit card issuer] to freeze your account, report fraud, or request a new card. If you shared your SSN or sensitive identity data, consider placing a :red[fraud alert or a security freeze] on your credit.")
                st.divider()
                st.write("2. Don't respond to the message in any way, including typing STOP, because it will confirm that your phone number is active and likely to respond to another text. Instead, :red[block the number and delete the text.] ")
                st.divider()
                st.write("3. If you are still unsure whether or not the message is real, please do an :red[extensive check] on the number and what it is asking for you to do. If it tells you something about your bank or something similar, please :red[call that platform directly from their website] instead of interacting with the message to confirm its authenticity.")
            elif predictionNumber == 2:
                st.write("1. Avoid clicking the link. It may lead to malware or a phishing scam. If you have already clicked a link or given information, please disconnect your device from the internet as soon as possible and run a malware check. If you entered sensitive info like passwords, reset them.")
                st.divider()
                st.write("2. Don't respond to the message in any way as doing so might confirm that your number is active, laeding you to get more spam texts. Instead, block the number and delete the text.")
                st.divider()
                st.write("3. If you are still unsure whether or not the message is truly spam, please do an :yellow[extensive check] on the number and what it is asking for you to do. If it tells you something about your bank or something similar, please :yellow[call that platform directly from their website] instead of interacting with the message to confirm its authenticity.")

    if st.button("Scan more Images/Text?", width='stretch'):
        st.session_state.image_bytes = None
        image = None
        st.rerun()
    st.caption("Scamurai is not 100% accurate. Please understand that some 'safe' results could be scams, or some 'scam' can really be something safe. If you feel as if our model get something wrong, feel free to research more about a message beyond our guide.", text_alignment='center')

def useTextLayout():
    newtext = st.session_state.uploaded_text
    predictionNumber = getprediction(newtext)
    st.title(":red[Scam]urai", text_alignment='center', icon="⚔️")
    col1, col2 = st.columns([3, 1])
    with col2:
        st_echarts(options=getOptions(predictionNumber, round(getconfidence(newtext))), height='200px', width='200px')
    with col1:
        st.space(size="small")
        st.space(size="xxsmall")
        st.title(getText(predictionNumber), text_alignment="center")

    col1, col2 = st.columns([2, 2])
    with col1:
        st.subheader("Scanned Text: ", text_alignment='center')
        with st.container(border=True):
            st.write(newtext)
    with col2:
        if predictionNumber == 0:
            st.write("1. We are pretty sure this is a :green[safe message!] However, our prediction model can be wrong. Please interact with it at your discretion.")
            st.divider()
            st.write("2. Remember, don't give :green[any sensitive info] that a complete stranger would need because it could always be a bad actor trying to get your information.")
        elif predictionNumber == 1:
            st.write("1. If you have already clicked a link or given information, please :red[disconnect your device from the internet] as soon as possible and :red[run a malware scan] for hidden threats. If you entered passwords or login details, :red[immediately change that information] on those platforms. If you shared financial information, :red[call your bank or credit card issuer] to freeze your account, report fraud, or request a new card. If you shared your SSN or sensitive identity data, consider placing a :red[fraud alert or a security freeze] on your credit.")
            st.divider()
            st.write("2. Don't respond to the message in any way, including typing STOP, because it will confirm that your phone number is active and likely to respond to another text. Instead, :red[block the number and delete the text.] ")
            st.divider()
            st.write("3. If you are still unsure whether or not the message is real, please do an :red[extensive check] on the number and what it is asking for you to do. If it tells you something about your bank or something similar, please :red[call that platform directly from their website] instead of interacting with the message to confirm its authenticity.")
        elif predictionNumber == 2:
            st.write("1. Avoid clicking the link. It may lead to malware or a phishing scam. If you have already clicked a link or given information, please disconnect your device from the internet as soon as possible and run a malware check. If you entered sensitive info like passwords, reset them.")
            st.divider()
            st.write("2. Don't respond to the message in any way as doing so might confirm that your number is active, laeding you to get more spam texts. Instead, block the number and delete the text.")
            st.divider()
            st.write("3. If you are still unsure whether or not the message is truly spam, please do an :yellow[extensive check] on the number and what it is asking for you to do. If it tells you something about your bank or something similar, please :yellow[call that platform directly from their website] instead of interacting with the message to confirm its authenticity.")
    if st.button("Scan more Images/Text?", width='stretch'):
            st.session_state.uploaded_text = None
            st.rerun()
    st.caption("Disclaimer: Scamurai is not 100% accurate. Please understand that some 'safe' results could be scams, or some 'scam' can really be something safe. If you feel as if our model get something wrong, feel free to research more about a message beyond our guide.", text_alignment='center')
        

def useWelcomeLayout():
    st.title(":red[Scam]urai - Malicious Image Detecting", width="stretch", text_alignment="center", anchor='false', icon="⚔️")
    st.text("To get started, please upload a string of text or an image. Our scamurai will take care of determining its danger.", width="stretch", text_alignment="center")

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.space(size="large")
        uploaded_image = st.file_uploader(label="Upload your image", type=('jpg', 'png', 'webp', 'avif'))
        uploaded_text = st.text_input(label="Or upload text")
        if uploaded_image:
            st.session_state.image_bytes = uploaded_image.getvalue()
            st.rerun()
        if uploaded_text:
            st.session_state.uploaded_text = uploaded_text
            st.rerun()
    st.space(size="xxlarge")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.caption("Disclaimer: Scamurai is not 100% accurate. Please understand that some 'safe' results could be scams, or some 'scam' can really be something safe. If you feel as if our model get something wrong, feel free to research more about a message beyond our guide.", text_alignment='justify')
    with col2:
        st.space(size='xxsmall')
        st.write(":blue[https://www.wikihow.com/Avoid-Scams]")

def getScannedText(image):
    imgFormatted = image.convert("RGB")
    text = pt.image_to_string(imgFormatted)
    return text

def getType(image):
    imgFormatted = image.convert("RGB")
    text = pt.image_to_string(imgFormatted)
    predictionType = getprediction(text)
    return predictionType

def grabConfidence(image):
    imgFormatted = image.convert("RGB")
    text = pt.image_to_string(imgFormatted)
    confidence = round(getconfidence(text))
    return confidence

def getText(number):
    #0 is safe, 1 is scam, 2 is spam
    string = ""
    if number == 0:
        string = "This is Likely a :green[Safe] Message"
    elif number == 1:
        string = "This is Likely a :red[Scam] Message"
    elif number == 2:
        string = "This is Likely a :yellow[Spam] Message"
    return string

def getOptions(number, confidenceNumber):
    if number == 0:
        data = [
                {"value": confidenceNumber, "name": "Safe"},
                {"value": 100-confidenceNumber, "name": "Unsure"},
            ]
        color1 = "#50C878"
        color2 = "#FF0000"
    elif number == 1:
        data = [
                {"value": confidenceNumber, "name": "Scam"},
                {"value": 100-confidenceNumber, "name": "Unsure"},
            ]
        color1 = "#FF0000"
        color2 = "#328B39"
    elif number == 2:
        data = [
                {"value": confidenceNumber, "name": "Spam"},
                {"value": 100-confidenceNumber, "name": "Unsure"},
            ]
        color1 = "#FFD700"
        color2 = "#328B39"

    options = {
        "title": {
            "text": (str(confidenceNumber) + "%"),
            "left": "center",
            "top": "center",
            "textStyle": {"fontSize": 32, "fontWeight": "bold"},
        },
        "tooltip": {"trigger": "item", "formatter": "{b}: {d}%"},
        "color": [color1, color2],
        "series": [
            {
                "type": "pie",
                "radius": ["50%", "80%"],
                "center": ["50%", "50%"],
                "avoidLabelOverlap": True,
                "itemStyle": {
                    "borderRadius": 8,
                    "borderColor": "#fff",
                    "borderWidth": 2
                },
                "label": {
                    "show": True,
                    "formatter": "{b}: {d}%",
                    "fontSize": 12
                },
                "labelLine": {"show": False, "length": 15, "length2": 10},
                "data": data,
            }
        ],

        }
    return options
        
if st.session_state.image_bytes is None and st.session_state.uploaded_text is None:
    useWelcomeLayout()
elif st.session_state.image_bytes: 
    useImageLayout()
elif st.session_state.uploaded_text:
    useTextLayout()




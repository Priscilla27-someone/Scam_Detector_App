import html
import re
import pandas as pd
import easyocr
import numpy as np
import streamlit as st
from PIL import Image, ImageOps

st.set_page_config(page_title="Scam Checker", layout="wide")

URL_RE = r"((?:https?://|www\.)[^\s<>]*[^\s<>.,;:?)'\"])"


def highlight_links(text, color="red"):
    parts = re.split(URL_RE, text)
    out = []
    for i, part in enumerate(parts):
        safe = html.escape(part)
        if i % 2 == 1:  # odd positions are the links
            out.append(
                f'<span style="background-color:{color}; color:white; '
                f'padding:0; border-radius:4px">{safe}</span>'
            )
        else:
            out.append(safe)
    return "".join(out).replace("\n", "<br>")


def preprocess(img, min_width=1600):
    img = img.convert("L")
    if np.array(img).mean() < 127:  # dark background -> invert
        img = ImageOps.invert(img)
    if img.width < min_width:
        scale = min_width / img.width
        img = img.resize(
            (int(img.width * scale), int(img.height * scale)), Image.LANCZOS
        )
    img = ImageOps.autocontrast(img)
    return ImageOps.expand(img, border=30, fill=255)


@st.cache_resource  # load the model once, not on every rerun
def get_reader():
    return easyocr.Reader(["en"])


st.sidebar.success("Select a page.")

col1, col2 = st.columns([2, 4])

with col1:
    text = st.text_input(
        "Enter a message below", "Text..."
    )
    if text:
        st.html(highlight_links(text))
    uploaded = st.file_uploader(
            "Upload an image", type=["png", "jpg", "jpeg", "webp"]
        )
    
    if uploaded:
        img = Image.open(uploaded)
        st.image(img)
    
        clean = preprocess(img)
        lines = get_reader().readtext(
                np.array(clean),
            detail=0,
            paragraph=True,
            width_ths=1.0,
        )
        ocr_text = " ".join(lines)
    
        st.text_area("Extracted text", ocr_text, height=200)
        if ocr_text.strip():
            st.html(highlight_links(ocr_text))

with col2:
    df = pd.DataFrame({
        "month": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], 
        "amount of scams":[100,500,250,1250,670,420,313,800,100,300,424,200]
    })
    st.line_chart(df, x="month", y="amount of scams")
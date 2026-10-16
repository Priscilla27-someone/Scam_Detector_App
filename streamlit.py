import streamlit as st
import pandas as pd
import re 
import html
import easyocr
import numpy as np
from PIL import Image, ImageOps

URL_RE = r"((?:https?://|www\.)[^\s<>]*[^\s<>.,;:?)'\"])"

def highlight_links(text, color="red"):
    parts = re.split(URL_RE, text)
    out = []

    for i, part in enumerate(parts):
        safe = html.escape(part)
        if i % 2 == 1: # this place is a link
            out.append(
                f'<span style="background-color:{color}; color:white; '
                f'padding:0; border-radius:4px">{safe}</span>'
            )
        else:
            out.append(safe)
    return "".join(out).replace("\n", "<br>")

text = st.text_input("Enter something", "Check out https://streamlit.io, it's great!")
if text:
    st.html(highlight_links(text))

def preprocess(img, min_width=1600):
    img = img.convert("L")
    if np.array(img).mean() < 127:
        img = ImageOps.invert(img)
    if img.width < min_width:
        scale = min_width / img.width
        img = img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)
    img = ImageOps.autocontrast(img)
    return ImageOps.expand(img, border=30, fill=255)

@st.cache_resource  # load the model once, not on every rerun
def get_reader():
    return easyocr.Reader(["en"])

uploaded = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "webp"])
ocr_text = ""

if uploaded:
    img = Image.open(uploaded)
    st.image(img)
    clean = preprocess(img)
    lines = get_reader().readtext(
        np.array(clean),
        detail=0,
        paragraph=True,
        width_ths=1.0
    )
    ocr_text = " ".join(lines)
    st.text_area("Extracted text", ocr_text, height = 200)
    if ocr_text.strip():
        st.html(highlight_links(ocr_text))

textbox_component = st.components.v2.component(
    "simple_textbox",
    html=
    
"""<label style='padding-right: 1em;' for='txt'>Enter text</label>
<input id='txt' type='text' />"""
    ,
    js=

"""export default function (component) {
  const { setStateValue, parentElement, data } = component;

  const label = parentElement.querySelector("label");
  label.innerText = data.label;

  const input = parentElement.querySelector("input");
  if (input.value !== data.value) {
    input.value = data.value ?? "";
  }

  input.onkeydown = (e) => {
    if (e.key === "Enter") {
      setStateValue("value", e.target.value);
    }
  };

  input.onblur = (e) => {
    setStateValue("value", e.target.value);
  };
}"""

)

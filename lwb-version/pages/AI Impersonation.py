import streamlit as st
import time
import numpy as np

audiopath = "deepfakeAudio.mp3"

st.set_page_config(page_title="How to prevent scams")
st.markdown("AI Generated Video & Audio Deepfakes")
st.sidebar.header("A comprehensive Guide")
st.write(":rainbow[Scams are detrimental!]")
st.audio(audiopath, format="audio/mp3")
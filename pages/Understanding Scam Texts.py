import streamlit as st
import pandas as pd
st.set_page_config(
    page_title = "Common Scams",
    layout="wide"
)

df = pd.DataFrame({
    'Amount': [17.8, 183, 1100, 1000, 4200, 6900, 10300, 12500, 16600, 20877],
    'Year': [2001, 2005, 2010, 2015, 2020, 2021, 2022, 2023, 2024, 2025]
})

st.dataframe(df, use_container_width=True)
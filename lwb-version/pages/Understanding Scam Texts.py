import streamlit as st
import pandas as pd
st.set_page_config(
    page_title = "Common Scams",
    layout="wide"
)

st.header(":red[Anti]Scam")
st.header("Scams: A Rampant Issue in the Modern World \n\n ", text_alignment="center")
st.write("")
st.write("")
st.write("")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Monetary loss due to cybercrime per year in millions", text_alignment='center')
    df = pd.DataFrame({
        'Millions': [17.8, 183, 1100, 1000, 4200, 6900, 10300, 12500, 16600, 20877],
        'Year': [2001, 2005, 2010, 2015, 2020, 2021, 2022, 2023, 2024, 2025]
    })


    st.bar_chart(
        data=df,
        x="Year",
        y="Millions",
        x_label = "Year",
        y_label = "$ Million",

        use_container_width=True)

    img1, img2, img3 = st.columns(3)
    with img1:
        st.image("ExampleScam.png", caption="A common fake USPS package scam. Link redacted for safety.", width="stretch")
    with img2:
        st.image("ExampleScam2.png", caption="A fake prize scam. Link redacted for safety.", width="stretch")
        st.image("ExampleScam4.png", caption="A fake verification scam. Phone # redacted for safety.", width="stretch")
    with img3:
        st.image("ExampleScam3.png", caption="A fake toll payment scam. Link redacted for safety.", width="stretch")

with col2:
    st.subheader(" What to look out for in spam/phishing emails or texts", text_alignment='center')
    st.markdown("    Frequently people receive junk messages or messages that are meant to [steal personal information]. It of great importance to know what to look out for to not fall into these traps. \n\n" \
    "1. Impersonal emails that could be addressed to anyone \n\n" \
    "2. Unexpected text messages from unknown numbers that… \n\n" \
    "a. Require personal information such as :red[password], :red[username], or :red[bank statements/numbers.]\n\n" 
    "b. Promote :red[fake deals] \n\n"
    "c. Promise :red[prize money] or :red[fake loans] \n\n" \
    "3. Unexpected emails/text that pretend to be another organization or person \n\n" \
    "a. Will say that they :red[suspect malicious activity] in your account \n\n"
    "b. Say that a :red[package has been delivered] when you haven’t actually ordered anything \n\n" \
    "c. Claim there are red:[payment issues] \n\n" \
    "d. If you are still not sure, :blue[always reach out to the company directly] to find out if there is actually an issue.\n\n" \
    "4. Never click on a link unless you're :blue[100% positive] it is not  fake email. Hackers can get your information through those links.")
    st.markdown("Companies will tell you how they need to receive sensitive information from you. Most of the time it’s not over email or text, but they do, you will know in advance if they are about to send an email or text to you requesting information.")
    st.caption("https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages")
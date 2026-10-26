import streamlit as st
import pandas as pd
st.set_page_config(
    page_title = "Common Scams",
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

st.title(":red[Scam]urai", text_alignment='center', icon="⚔️")

st.header(":red[Scams]: A Rampant Issue in the Modern World \n\n ", text_alignment="center")
st.space(size="medium")

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
    st.image("prj-mac_version/ExampleScam.png", caption="A common fake USPS package scam. Link redacted for safety.", width="stretch")
with img2:
    st.image("prj-mac_version/ExampleScam2.png", caption="A fake prize scam. Link redacted for safety.", width="stretch")
    st.image("prj-mac_version/ExampleScam4.png", caption="A fake verification scam. Phone # redacted for safety.", width="stretch")
with img3:
    st.image("prj-mac_version/ExampleScam3.png", caption="A fake toll payment scam. Link redacted for safety.", width="stretch")

st.markdown("Frequently people receive junk messages or messages that are meant to [steal personal information]. It of great importance to know what to look out for to not fall into these traps.", text_alignment='center')
st.subheader("Look out for these common signs", text_alignment='center')
with st.container(border=True):
    st.markdown("Impersonal emails that could be addressed to anyone", text_alignment='center')
with st.container(border=True):
    st.markdown("Unexpected text messages from unknown numbers that…", text_alignment='center') 
    st.markdown("Require personal information such as :red[password], :red[username], or :red[bank statements/numbers.]", text_alignment='center', width='stretch')
    st.markdown("Promote :red[fake deals]", text_alignment='center')
    st.markdown("Promise :red[prize money] or :red[fake loans]", text_alignment='center',)
with st.container(border=True):
    st.markdown("Unexpected emails/text that pretend to be another organization or person", text_alignment='center')
with st.container(border=True):
    st.markdown("Will say that they :red[suspect malicious activity] in your account", text_alignment='center')
with st.container(border=True):
    st.markdown("Say that a :red[package has been delivered] when you haven’t actually ordered anything", text_alignment='center')
with st.container(border=True):
    st.markdown("Claim there are :red[payment issues]", text_alignment='center')
st.subheader("If you are still not sure, :blue[always reach out to the company directly] to find out if there is actually an issue. Never click on a link unless you're :blue[100% positive] it is not a fake email.", text_alignment='justify')
st.caption("https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages", text_alignment='center')



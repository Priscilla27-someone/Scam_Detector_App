import streamlit as st
import time
import numpy as np

audiopath = "deepfakeAudio.mp3"

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

st.set_page_config(page_title="Recent Scams")

st.title(":red[Scam]urai", text_alignment='center', icon="⚔️")

st.title("Looking at Scams in Recent History", text_alignment = 'center')
st.markdown("Scams aren't anything new. Here is how scams have impacted the internet for decades.", text_alignment='center')      
st.divider()
col1, col2, col3 = st.columns([2, 2, 2])
with col1:
    with st.container(border=True):
        st.markdown('Nigerian Prince Emails', text_alignment='center')
        st.markdown('Estimated Impact: :green[$60,000,000]', text_alignment='center')
        st.markdown('Year: :blue[1990s]', text_alignment='center')
        st.markdown("In this scam, someone will act as a wealthy prince needing an upfront of money (often a few hundred dollars) while promising to give you millions in return. They will run off with the money after receiving it.", text_alignment='center')
        st.image("prj-mac_version/NigerianPrince.png")
        st.caption("https://en.wikipedia.org/wiki/Advance-fee_scam", text_alignment='center')
    with st.container(border=True):
        st.markdown('Tinder Swindler', text_alignment='center')
        st.markdown('Estimated Impact: :green[$10,000,000]', text_alignment='center')
        st.markdown('Year: :blue[2017-2019]', text_alignment='center')
        st.markdown("In this scam, a con man used Tinder to swindle money by acting as a rich Russian man who needed money to avoid 'sudden danger'. After recieving the money, the man would disappear.", text_alignment='center')
        st.image("prj-mac_version/TinderSwindler.webp")
        st.caption("https://en.wikipedia.org/wiki/The_Tinder_Swindler", text_alignment='center')
with col2:
    with st.container(border=True):
            st.markdown('Fake Tech Support', text_alignment='center')
            st.markdown('Estimated Impact: :green[$1,400,000,000 Anually]', text_alignment='center')
            st.markdown('Year: :blue[2008-Current]', text_alignment='center')
            st.markdown("In this scam, criminals will pretend to be representatives from major tech companies to trick you into believing your device has a severe problem. Then, they will show you fake 'dangerous files' and try to coerce you into providing sensitive info or money.", text_alignment='center')
            st.image("prj-mac_version/TechSupportScam.jpg")
            st.caption("https://en.wikipedia.org/wiki/Technical_support_scam", text_alignment='center')
    with st.container(border=True):
            st.markdown('Google Docs Phishing Worm', text_alignment='center')
            st.markdown('Estimated Impact: :yellow[1,000,000 Gmail Users]', text_alignment='center')
            st.markdown('Year: :blue[2017]', text_alignment='center')
            st.markdown("Victims recieved an email from a trusted contact asking them to open a shared document on Google Docs. Then, the page asked them to grant access to a fake 'Google Docs' web application, which was able to give scammers access to Gmail Inboxes and contact lists.", text_alignment='center')
            st.image("prj-mac_version/GoogleScam.png")
            st.caption("https://www.wired.com/story/google-docs-scams-threat-phishing/", text_alignment='center')
with col3:
    with st.container(border=True):
            st.markdown('Fake Login Scam', text_alignment='center')
            st.markdown('Estimated Impact: :yellow[50,000,000 Google Users]', text_alignment='center')
            st.markdown('Year: :blue[2023-2026]', text_alignment='center')
            st.markdown("Criminals created fake login pages and coerced people into believing they were logging into the real page to steal login information.", text_alignment='center')
            st.image("prj-mac_version/FakeLoginScam.jpg")
            st.caption("https://blog.mega.io/fake-google-security-alert-email", text_alignment='center')
    with st.container(border=True):
            st.markdown('Fake Shopping & Delivery', text_alignment='center')
            st.markdown('Estimated Impact: :green[$470,000,000]', text_alignment='center')
            st.markdown('Year: :blue[2022-Current]', text_alignment='center')
            st.markdown("Victims recieved a text message claiming that a delivery was delayed or some information needs confirmation. A counterfeit delivery website would then ask for sensitive information.", text_alignment='center')
            st.image("prj-mac_version/FakeDeliveryScam.jpg")
            st.caption("https://www.aba.com/advocacy/community-programs/consumer-resources/protect-your-money/package-delivery-scams", text_alignment='center')
st.divider()

st.header("What can we learn?", text_alignment='center')
st.markdown("Most of the time, bad actors will attempt to use the credibility of a large service by impersonation in order to make you hand over sensitive info. Being prepared means being able to recognize the common signs of a scam.", text_alignment='center')
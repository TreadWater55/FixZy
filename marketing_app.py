import streamlit as st

# Set page config
st.set_page_config(page_title="FixZy - Home Repair Assistant", page_icon="🔧", layout="centered")

# Centered content
st.markdown("<h1 style='text-align: center;'>🔧 Welcome to FixZy 🔧</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Your Smart DIY Home Repair Assistant</h3>", unsafe_allow_html=True)

st.write("---")

st.markdown("""
<div style='text-align: center; font-size:18px;'>
🏠 Fix things around the house easily<br>
🛠️ Step-by-step professional fixes<br>
🔍 Find the right tools and tips fast<br>
🚀 Get back to living, not guessing
</div>
""", unsafe_allow_html=True)

st.write("---")

# Big button to launch app
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("🚀 Launch FixZy Now"):
    st.markdown("<meta http-equiv='refresh' content='0; url=https://sldvxrrz3qozstksxk4bzw.streamlit.app/' />", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

st.markdown("<p style='text-align: center; font-size:14px;'>Built with ❤️ by the FixZy Team</p>", unsafe_allow_html=True)

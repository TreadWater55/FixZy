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

# Correct Launch Button
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.markdown("[🚀 Launch FixZy Now](https://sldvxrrz3qozstksxk4bzw.streamlit.app/)", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# Email signup form
st.subheader("📧 Stay Updated with FixZy!")

with st.form(key="email_form", clear_on_submit=True):
    user_email = st.text_input("Enter your email to get updates:")
    submit_email = st.form_submit_button("Subscribe")

    if submit_email:
        if user_email:
            # Save the email (append to file)
            with open("emails_collected.txt", "a") as f:
                f.write(user_email + "\n")
            st.success("✅ Thanks for subscribing! We'll keep you updated.")
        else:
            st.error("❌ Please enter a valid email.")

st.write("---")

st.markdown("<p style='text-align: center; font-size:14px;'>Built with ❤️ by the FixZy Team</p>", unsafe_allow_html=True)

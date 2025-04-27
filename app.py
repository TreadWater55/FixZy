import streamlit as st
import os
import json
import random
from fixzy_backend import synthesize_response

# Load category-specific fixes
def load_fixes_by_category(category):
    try:
        with open("data/diy_issues.json", "r") as f:
            data = json.load(f)
        return [item for item in data if item["category"].lower() == category.lower()]
    except Exception as e:
        st.error(f"Error loading fixes: {e}")
        return []

# Random loading messages
loading_messages = [
    "🔧 Grabbing your tools...",
    "🔍 Inspecting the issue...",
    "🛠️ Finding the best fix...",
    "🏠 Getting ready to repair...",
    "✍️ Writing your Fixzy solution..."
]

# Page config
st.set_page_config(page_title="Fixzy", layout="centered")

# Sidebar Navigation
st.sidebar.title("🔧 Fixzy Navigation")
page = st.sidebar.radio("Go to:", ["Home", "About", "FAQ", "Need Help?"])

# HOME PAGE
if page == "Home":
    try:
        st.image("static/fixzy_logo.png", width=200)
    except FileNotFoundError:
        st.warning("Logo not found. Please ensure 'fixzy_logo.png' exists in the static folder.")

    st.title("🏠 Welcome to Fixzy")
    st.subheader("We’ve scoured the web for answers — so you don’t have to.")

    search_query = st.text_input("🔍 What needs fixing today?")

    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    if search_query == "":
        st.session_state.submitted = False

    if st.button("Get My Fix", use_container_width=True):
        st.session_state.submitted = True

    if st.session_state.submitted and search_query:
        with st.spinner(random.choice(loading_messages)):
            try:
                result_data = synthesize_response(search_query)

                if isinstance(result_data, dict):
                    best_match = result_data
                    st.markdown("<h2 style='text-align: center;'>🔧 Fixzy Suggestions</h2>", unsafe_allow_html=True)
                    st.markdown(f"### 🛠️ Problem: {best_match['problem']}")
                    st.info(f"**Likely Cause:** {best_match['cause']}")
                    st.success(f"**Recommended Fix:** {best_match['fix']}")
                    st.warning(f"**Tools Needed:** {', '.join(best_match['tools']) if best_match['tools'] else 'None'}")
                    st.warning(f"**Materials Needed:** {', '.join(best_match['materials']) if best_match['materials'] else 'None'}")
                    st.code(f"Estimated Time: {best_match['time']}\nDifficulty: {best_match['difficulty']}", language="markdown")

                    if best_match.get("video"):
                        st.markdown("🎥 **Watch Tutorial:**")
                        st.video(best_match["video"])
                    else:
                        st.info("🎥 Tutorial coming soon!")

                    st.write("---")

                else:
                    st.markdown("<h2 style='text-align: center;'>🔧 Fixzy Suggestions</h2>", unsafe_allow_html=True)
                    sections = result_data.split("\n")
                    for section in sections:
                        if "Likely Cause:" in section:
                            st.info(section.replace("Likely Cause:", "**Likely Cause:**"))
                        elif "Recommended Fix:" in section:
                            st.success(section.replace("Recommended Fix:", "**Recommended Fix:**"))
                        elif "Tools Needed:" in section or "Materials Needed:" in section:
                            st.warning(section.replace("Tools Needed:", "**Tools Needed:**").replace("Materials Needed:", "**Materials Needed:**"))
                        elif "Estimated Time:" in section or "Difficulty:" in section:
                            st.code(section.replace("Estimated Time:", "**Estimated Time:**").replace("Difficulty:", "**Difficulty:**"), language="markdown")
                        elif section.strip():
                            st.markdown(section)

                    st.info("🎥 Tutorial coming soon!")
                    st.write("---")

            except Exception as e:
                st.error(f"Something went wrong while fetching your fix: {e}")

    st.subheader("🛠️ Popular Categories")
    category_icons = {
        "Plumbing": "🛁",
        "Electrical": "⚡",
        "HVAC": "❄️",
        "Roofing": "🏠",
        "Flooring": "🪵",
        "Appliances": "🔧"
    }

    for category, icon in category_icons.items():
        if st.button(f"{icon} {category}", key=f"btn_{category.lower().replace(' ', '_')}", use_container_width=True):
            with st.spinner(f"🔎 Loading {category} fixes..."):
                selected_fixes = load_fixes_by_category(category)
                if selected_fixes:
                    st.markdown(f"<h3 style='text-align: center;'>{icon} {category} Fixes</h3>", unsafe_allow_html=True)
                    for fix in selected_fixes:
                        with st.expander(f"🛠️ {fix['problem']}", expanded=False):
                            st.write(f"**Cause:** {fix['cause']}")
                            st.write(f"**Difficulty:** {fix['difficulty']}")
                            st.write(f"**Time Estimate:** {fix['time']}")
                            st.write(f"**Tools Needed:** {', '.join(fix['tools']) if fix['tools'] else 'None'}")
                            st.write(f"**Materials Needed:** {', '.join(fix['materials']) if fix['materials'] else 'None'}")
                            st.markdown("**Step-by-Step:**")
                            st.info(fix['plain_fix'])
                else:
                    st.warning(f"No fixes found yet for {category}. Coming soon!")

    st.divider()
    st.subheader("🚀 Quick Links")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("View All Fixes", use_container_width=True):
            st.info("Redirecting to the full list... (Coming soon)")

    with col2:
        if st.button("FAQ", use_container_width=True):
            st.info("Opening FAQ page...")

    with col3:
        if st.button("Need Help?", use_container_width=True):
            st.info("Opening Help page...")

elif page == "About":
    st.title("ℹ️ About Fixzy")
    st.write("Fixzy is your smart DIY repair assistant — designed to help you fix things around the house yourself, with the confidence and clarity of a seasoned pro.")
    st.write("- 💪 Easy-to-follow fixes")
    st.write("- ⚙️ Smart tool + material suggestions")
    st.write("- 💬 Clear, pro-grade explanations")
    st.success("Fixzy doesn't just show you what to do—it teaches you how to fix it.")

elif page == "FAQ":
    st.title("❓ Frequently Asked Questions")
    st.write("- **What is Fixzy?** Fixzy is an AI-powered DIY repair assistant.")
    st.write("- **Is it free?** Yes, Fixzy is free while we continue to grow and improve.")
    st.write("- **Can I submit my own fixes?** Coming soon! You'll be able to share your home repair victories.")

elif page == "Need Help?":
    st.title("🚨 Need Help?")
    st.write("If you're stuck, can't find your issue, or need guidance — Fixzy has your back.")
    user_input = st.text_area("📝 Describe your problem here:", height=150)
    if user_input:
        st.success("✅ Thanks for submitting your issue! We'll use this to improve Fixzy.")
    st.info("📧 Email support is coming soon!")
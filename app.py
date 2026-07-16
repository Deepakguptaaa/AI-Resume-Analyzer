import streamlit as st

from views.dashboard_page import dashboard_page
from views.resume_page import resume_page
from views.job_match_page import job_match_page
from views.optimizer_page import optimizer_page
from views.cover_letter_page import cover_letter_page
from views.interview_page import interview_page

# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="AI Career Assistant Pro",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.markdown("""
<div class="sidebar-title">🚀 AI Career Assistant</div>
<div class="sidebar-subtitle">AI-powered Career Toolkit</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📄 Resume Analysis",
        "🎯 Job Match",
        "✨ Resume Optimizer",
        "💌 Cover Letter",
        "🎤 Interview Prep"
    ]
)

# -----------------------------
# Navigation
# -----------------------------

if page == "🏠 Dashboard":
    dashboard_page()

elif page == "📄 Resume Analysis":
    resume_page()

elif page == "🎯 Job Match":
    job_match_page()

elif page == "✨ Resume Optimizer":
    optimizer_page()

elif page == "💌 Cover Letter":
    cover_letter_page()

elif page == "🎤 Interview Prep":
    interview_page()
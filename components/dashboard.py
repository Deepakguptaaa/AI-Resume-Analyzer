import streamlit as st
import re
from components.charts import ats_gauge


def get_section(text, section_name):
    pattern = rf"# {re.escape(section_name)}\n(.*?)(?=\n# |\Z)"
    match = re.search(pattern, text, re.DOTALL)

    if match:
        return match.group(1).strip()

    return "Not Available"


def display_dashboard(result):

    st.header("📊 Resume Analysis Dashboard")

    # ATS Score
    score = 0
    match = re.search(r"# ATS Score\s*(\d+)", result)

    if match:
        score = int(match.group(1))

    ats_gauge(score)
    
    
    if score >= 85:
     st.markdown(
        '<p class="score-good">🟢 Excellent ATS Resume</p>',
        unsafe_allow_html=True
    )
    elif score >= 70:
     st.markdown(
        '<p class="score-medium">🟡 Good Resume</p>',
        unsafe_allow_html=True
    )
    else:
     st.markdown(
        '<p class="score-low">🔴 Needs Improvement</p>',
        unsafe_allow_html=True
    )    

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💪 Strengths")
        st.success(get_section(result, "Strengths"))

    with col2:
        st.subheader("⚠ Weaknesses")
        st.warning(get_section(result, "Weaknesses"))

    st.divider()

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("🛠 Technical Skills")
        st.info(get_section(result, "Technical Skills Found"))

    with col4:
        st.subheader("🎯 Missing Skills")
        st.error(get_section(result, "Missing Skills"))

    st.divider()

    col5, col6 = st.columns(2)

    with col5:
        st.subheader("📚 Certifications")
        st.success(get_section(result, "Certifications Recommended"))

    with col6:
        st.subheader("🚀 Suggested Projects")
        st.info(get_section(result, "Suggested Projects"))

    st.divider()

    st.subheader("💡 Resume Improvement Suggestions")
    st.write(get_section(result, "Resume Improvement Suggestions"))
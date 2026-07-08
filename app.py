import streamlit as st
from dotenv import load_dotenv
import os

from utils.pdf_reader import extract_resume_text
from utils.gemini import (
    analyze_resume,
    analyze_job_match,
    optimize_resume
)
from utils.pdf_report import create_pdf
from components.dashboard import display_dashboard

# -----------------------------
# Load CSS
# -----------------------------

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# -----------------------------
# Load Environment Variables
# -----------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# -----------------------------
# Page Settings
# -----------------------------

st.set_page_config(
    page_title="AI Resume Analyzer Pro",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer Pro")

st.markdown("""
### 🚀 AI-powered Resume Review

Upload your resume and receive:

- 🎯 ATS Score
- 💪 Strengths
- ⚠️ Weaknesses
- 🛠️ Technical Skills
- ❌ Missing Skills
- 📚 Recommended Certifications
- 🚀 Suggested Projects
- 📋 Job Match Analysis
- ✨ AI Resume Optimization
""")

st.divider()

# -----------------------------
# Upload Resume
# -----------------------------

uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

resume_text = ""

if uploaded_file:

    resume_text = extract_resume_text(uploaded_file)

    st.success("✅ Resume uploaded successfully!")

    with st.expander("📄 View Extracted Resume"):

        st.text_area(
            "Resume Text",
            resume_text,
            height=300
        )

    st.divider()

    # -----------------------------
    # Resume Analysis
    # -----------------------------

    st.subheader("🤖 Resume Analysis")

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            try:

                result = analyze_resume(resume_text)

                display_dashboard(result)

                pdf_file = create_pdf(result)

                with open(pdf_file, "rb") as file:

                    st.download_button(
                        label="📄 Download PDF Report",
                        data=file,
                        file_name="Resume_Analysis_Report.pdf",
                        mime="application/pdf"
                    )

            except Exception as e:

                st.error(e)

    st.divider()

    # -----------------------------
    # Job Description Match
    # -----------------------------

    st.subheader("🎯 Job Description Match")

    job_description = st.text_area(
        "Paste Job Description",
        height=220,
        placeholder="Paste the company's job description here..."
    )

    if job_description:

        if st.button("Analyze Job Match"):

            with st.spinner("Comparing Resume with Job Description..."):

                try:

                    result = analyze_job_match(
                        resume_text,
                        job_description
                    )

                    display_dashboard(result)

                    pdf_file = create_pdf(result)

                    with open(pdf_file, "rb") as file:

                        st.download_button(
                            label="📄 Download Job Match Report",
                            data=file,
                            file_name="Job_Match_Report.pdf",
                            mime="application/pdf"
                        )

                except Exception as e:

                    st.error(e)

    st.divider()

    # -----------------------------
    # AI Resume Optimizer
    # -----------------------------

    st.subheader("✨ AI Resume Optimizer")

    st.write(
        "Improve your resume with ATS-friendly wording, stronger action verbs, and professional formatting."
    )

    if st.button("✨ Optimize My Resume"):

        with st.spinner("Optimizing Resume..."):

            try:

                optimized_resume = optimize_resume(resume_text)

                st.success("✅ Resume Optimized Successfully!")

                st.text_area(
                    "Optimized Resume",
                    optimized_resume,
                    height=500
                )

                st.download_button(
                    label="📥 Download Optimized Resume (.txt)",
                    data=optimized_resume,
                    file_name="Optimized_Resume.txt",
                    mime="text/plain"
                )

            except Exception as e:

                st.error(e)
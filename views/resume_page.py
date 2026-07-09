import streamlit as st
from dotenv import load_dotenv
import os

from utils.pdf_reader import extract_resume_text
from utils.gemini import analyze_resume
from utils.pdf_report import create_pdf
from components.dashboard import display_dashboard

# -----------------------------
# Load API
# -----------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


def resume_page():

    st.title("📄 Resume Analysis")

    st.write(
        "Upload your resume and receive a complete AI-powered ATS analysis."
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"],
        key="resume_upload"
    )

    if uploaded_file:

        resume_text = extract_resume_text(uploaded_file)

        st.success("✅ Resume uploaded successfully!")

        with st.expander("View Resume"):

            st.text_area(
                "Resume Text",
                resume_text,
                height=300
            )

        st.divider()

        if st.button(
            "🤖 Analyze Resume",
            key="resume_analysis_btn"
        ):

            with st.spinner("Analyzing Resume..."):

                try:

                    result = analyze_resume(resume_text)

                    display_dashboard(result)

                    pdf_file = create_pdf(result)

                    with open(pdf_file, "rb") as file:

                        st.download_button(

                            "📄 Download PDF Report",

                            data=file,

                            file_name="Resume_Report.pdf",

                            mime="application/pdf"

                        )

                except Exception as e:

                    st.error(e)
import streamlit as st

import streamlit as st

from utils.gemini import analyze_job_match
from components.dashboard import display_dashboard
from utils.pdf_report import create_pdf
from utils.pdf_reader import extract_resume_text


def job_match_page():

    st.title("🎯 Job Description Match")

    st.write(
        "Compare your resume with a job description and get an ATS match score."
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"],
        key="job_match_resume"
    )

    if uploaded_file:

        resume_text = extract_resume_text(uploaded_file)

        st.success("✅ Resume uploaded successfully!")

        job_description = st.text_area(
            "Paste Job Description",
            height=250,
            placeholder="Paste company job description here..."
        )

        if job_description:

            if st.button(
                "Analyze Job Match",
                key="job_match_btn"
            ):

                with st.spinner("Analyzing Match..."):

                    try:

                        result = analyze_job_match(
                            resume_text,
                            job_description
                        )

                        display_dashboard(result)

                        pdf_file = create_pdf(result)

                        with open(pdf_file, "rb") as file:

                            st.download_button(
                                label="📄 Download Match Report",
                                data=file,
                                file_name="Job_Match_Report.pdf",
                                mime="application/pdf"
                            )

                    except Exception as e:

                        st.error(e)
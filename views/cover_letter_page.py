import streamlit as st

from utils.pdf_reader import extract_resume_text
from utils.gemini import generate_cover_letter


def cover_letter_page():

    st.title("💌 AI Cover Letter Generator")

    st.write(
        "Generate a personalized cover letter using your resume and a job description."
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"],
        key="cover_resume"
    )

    if uploaded_file:

        resume_text = extract_resume_text(uploaded_file)

        st.success("✅ Resume uploaded successfully!")

        job_description = st.text_area(
            "Paste Job Description",
            height=250,
            placeholder="Paste the company's job description here..."
        )

        if job_description:

            if st.button(
                "💌 Generate Cover Letter",
                key="cover_btn"
            ):

                with st.spinner("Generating Cover Letter..."):

                    try:

                        cover_letter = generate_cover_letter(
                            resume_text,
                            job_description
                        )

                        st.success("✅ Cover Letter Generated!")

                        st.text_area(
                            "Cover Letter",
                            cover_letter,
                            height=500
                        )

                        st.download_button(
                            "📄 Download Cover Letter",
                            cover_letter,
                            file_name="Cover_Letter.txt",
                            mime="text/plain"
                        )

                    except Exception as e:

                        st.error(e)
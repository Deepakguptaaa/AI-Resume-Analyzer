import streamlit as st

from utils.pdf_reader import extract_resume_text
from utils.gemini import optimize_resume


def optimizer_page():

    st.title("✨ AI Resume Optimizer")

    st.write(
        "Improve your resume with ATS-friendly wording, stronger action verbs, and professional formatting suggestions."
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"],
        key="optimizer_resume"
    )

    if uploaded_file:

        resume_text = extract_resume_text(uploaded_file)

        st.success("✅ Resume uploaded successfully!")

        with st.expander("View Resume"):

            st.text_area(
                "Resume",
                resume_text,
                height=300
            )

        if st.button(
            "✨ Optimize Resume",
            key="optimizer_btn"
        ):

            with st.spinner("Optimizing Resume..."):

                try:

                    optimized_resume = optimize_resume(resume_text)

                    st.success("✅ Resume Optimized!")

                    st.text_area(
                        "Optimized Resume",
                        optimized_resume,
                        height=450
                    )

                    st.download_button(
                        "📄 Download Optimized Resume",
                        optimized_resume,
                        file_name="Optimized_Resume.txt",
                        mime="text/plain"
                    )

                except Exception as e:

                    st.error(e)
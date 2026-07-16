import streamlit as st
st.write("Interview page loaded")
from utils.pdf_reader import extract_resume_text
from utils.gemini import generate_interview_questions


def interview_page():

    st.title("🎤 AI Interview Preparation")

    st.write(
        "Generate personalized interview questions based on your resume."
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"],
        key="interview_resume"
    )

    if uploaded_file:

        resume_text = extract_resume_text(uploaded_file)

        st.success("✅ Resume uploaded successfully!")

        if st.button(
            "🎤 Generate Interview Questions",
            key="interview_btn"
        ):

            with st.spinner("Preparing Interview Questions..."):

                try:

                    interview = generate_interview_questions(
                        resume_text
                    )

                    st.success("✅ Interview Guide Ready!")

                    st.markdown(interview)

                    st.download_button(
                        "📄 Download Interview Guide",
                        interview,
                        file_name="Interview_Preparation.txt",
                        mime="text/plain"
                    )

                except Exception as e:

                    st.error(e)
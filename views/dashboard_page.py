import streamlit as st


def dashboard_page():

    st.markdown("""
    <div class="hero">
        <h1>🚀 AI Career Assistant Pro</h1>
        <p>
            Analyze resumes, match job descriptions, optimize content, generate cover letters,
            and prepare for interviews with the power of Google Gemini AI.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("✨ Core Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📄</div>
            <div class="feature-title">Resume Analysis</div>
            <div class="feature-desc">
                Get ATS scores, strengths, weaknesses, missing skills, and personalized improvement suggestions.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Job Match</div>
            <div class="feature-desc">
                Compare your resume against any job description and discover missing keywords and skills.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">✨</div>
            <div class="feature-title">Resume Optimizer</div>
            <div class="feature-desc">
                Rewrite your resume with stronger action verbs and ATS-friendly professional language.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col4, col5 = st.columns(2)

    with col4:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💌</div>
            <div class="feature-title">Cover Letter Generator</div>
            <div class="feature-desc">
                Generate tailored cover letters using your resume and the target job description.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎤</div>
            <div class="feature-title">Interview Preparation</div>
            <div class="feature-desc">
                Receive HR, technical, AI/ML, and project-based interview questions with preparation tips.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("⚡ Quick Start")

    st.markdown("""
    <div class="feature-card">
        <ol>
            <li>Upload your resume in PDF format.</li>
            <li>Analyze your ATS score and resume quality.</li>
            <li>Compare it with a target job description.</li>
            <li>Optimize weak sections automatically.</li>
            <li>Generate a personalized cover letter.</li>
            <li>Prepare for interviews with AI-generated questions.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        Built with ❤️ using <b>Python</b> • <b>Streamlit</b> • <b>Google Gemini AI</b>
    </div>
    """, unsafe_allow_html=True)
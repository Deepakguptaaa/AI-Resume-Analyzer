import streamlit as st


def show_metric_cards(score, strengths, weaknesses, skills):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🎯 ATS Score",
            f"{score}/100"
        )

    with col2:
        st.metric(
            "💪 Strengths",
            strengths
        )

    with col3:
        st.metric(
            "⚠️ Weaknesses",
            weaknesses
        )

    with col4:
        st.metric(
            "🛠 Skills",
            skills
        )
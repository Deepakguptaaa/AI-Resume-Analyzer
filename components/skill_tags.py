import streamlit as st


def show_skill_tags(skills_text):

    skills = []

    for line in skills_text.split("\n"):

        line = line.replace("-", "").strip()

        if line:
            skills.append(line)

    if not skills:
        st.info("No skills found.")
        return

    cols = st.columns(3)

    for i, skill in enumerate(skills):

        with cols[i % 3]:
            st.success(f"🏷 {skill}")
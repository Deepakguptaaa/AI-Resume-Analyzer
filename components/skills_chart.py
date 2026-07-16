import streamlit as st
import matplotlib.pyplot as plt


def show_skills_chart(skills_text):

    categories = {
        "Programming": 0,
        "Machine Learning": 0,
        "Database": 0,
        "Tools": 0,
        "Others": 0
    }

    programming = [
        "python", "java", "c++", "c", "javascript"
    ]

    ml = [
        "machine learning",
        "tensorflow",
        "keras",
        "pytorch",
        "scikit-learn",
        "pandas",
        "numpy"
    ]

    database = [
        "sql",
        "mysql",
        "mongodb",
        "postgresql"
    ]

    tools = [
        "git",
        "github",
        "docker",
        "streamlit",
        "flask",
        "django"
    ]

    for line in skills_text.lower().split("\n"):

        skill = line.replace("-", "").strip()

        if not skill:
            continue

        if any(word in skill for word in programming):
            categories["Programming"] += 1

        elif any(word in skill for word in ml):
            categories["Machine Learning"] += 1

        elif any(word in skill for word in database):
            categories["Database"] += 1

        elif any(word in skill for word in tools):
            categories["Tools"] += 1

        else:
            categories["Others"] += 1

    labels = []
    values = []

    for key, value in categories.items():
        if value > 0:
            labels.append(key)
            values.append(value)

    if not values:
        return

    fig, ax = plt.subplots(figsize=(5, 5))

    ax.pie(
        values,
        labels=labels,
        autopct="%1.0f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)
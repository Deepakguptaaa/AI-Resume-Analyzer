import plotly.graph_objects as go
import streamlit as st


def ats_gauge(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            domain={"x": [0, 1], "y": [0, 1]},
            title={
                "text": "<b>ATS Score</b>",
                "font": {"size": 28}
            },
            number={
                "suffix": "/100",
                "font": {"size": 40}
            },
            gauge={
                "axis": {
                    "range": [0, 100]
                },
                "bar": {
                    "thickness": 0.35
                },
                "steps": [
                    {"range": [0, 40], "color": "#ff4b4b"},
                    {"range": [40, 70], "color": "#f7b500"},
                    {"range": [70, 100], "color": "#00cc96"},
                ],
            },
        )
    )

    fig.update_layout(
        height=350,
        margin=dict(l=20, r=20, t=50, b=20),
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
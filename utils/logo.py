import streamlit as st


def set_logo():
    _, logo_col, _ = st.columns([5, 4, 5])

    with logo_col:
        st.image("static/img/logo_avanza.webp", output_format="png")
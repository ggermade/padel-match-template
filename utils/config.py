import streamlit as st


def change_language() -> None:
    st.header("Settings")
    language = st.selectbox("Elige Idioma / Select Language", ["English", "Spanish"])
    if language == "English":
        set_language("en")
    else:
        set_language("es")

def set_language(language: str) -> None:
    st.session_state["language"] = language

def get_language() -> str:
    return st.session_state.get("language", "es")
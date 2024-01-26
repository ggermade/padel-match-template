import streamlit as st

from utils.translation import Translation


def set_language(language: str) -> None:
    st.session_state["language"] = language


def get_language(tl: Translation) -> str:
    language = st.session_state.get("language")

    if language:
        return tl.language_format_func(language)
    else:
        return "es"

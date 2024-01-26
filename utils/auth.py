import streamlit as st

from utils import translation as tl


def is_user_logged_in() -> bool:
    return st.session_state.get("user_logged_in", False)

def set_user_logged_in(value: bool) -> None:
    st.session_state["user_logged_in"] = value

def show_login_page() -> None:
    st.header(tl.LOGIN_TITLE)
    username = st.text_input(tl.USERNAME)
    password = st.text_input(tl.PASSWORD, type="password")
    login_button = st.button(tl.LOGIN_BUTTON)
    
    if login_button:
        if username == "admin" and password == "123":
            st.success("Logged in as admin")
            set_user_logged_in(True)
            st.rerun()
        else:
            st.error("Incorrect username or password")

def logout() -> None:
    set_user_logged_in(False)
    st.rerun()
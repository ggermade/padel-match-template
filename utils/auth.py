import streamlit as st

from utils.translation import Translation


def is_user_logged_in() -> bool:
    return st.session_state.get("user_logged_in", False)

def set_user_logged_in(value: bool) -> None:
    st.session_state["user_logged_in"] = value

def login_page(tl: Translation) -> None:
    st.header(tl.LOGIN_TITLE)

    with st.form(key="login-form", border=False):
        username = st.text_input(tl.USERNAME)
        password = st.text_input(tl.PASSWORD, type="password")
        
        if st.form_submit_button(tl.LOGIN_BUTTON):
            if username == "admin" and password == "123":
                st.success("Logged in as admin")
                set_user_logged_in(True)
            else:
                st.error("Incorrect username or password")
                set_user_logged_in(False)
    if is_user_logged_in():
        st.balloons()
        st.rerun()

def logout() -> None:
    set_user_logged_in(False)
    st.rerun()
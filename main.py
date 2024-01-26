import streamlit as st

from questions import show_questionnaire
from utils import translation as tl
from utils.auth import is_user_logged_in, logout, show_login_page
from utils.config import get_language

lang: str = get_language()

# Step 1: Create a Streamlit app with a login page
def main():
    # Show image logo at static/img/logo_avanza.webp
    _, logo_col, _ = st.columns([5, 4, 5])

    with logo_col:
        st.image("static/img/logo_avanza.webp", output_format="png")


    if is_user_logged_in():
        if st.button(tl.LOGOUT_BUTTON):
            logout()
        
    st.title(tl.MAIN_TITLE)
    
    # Step 2: Implement user authentication system
    if not is_user_logged_in():
        show_login_page()

    else:
        show_questionnaire()

if __name__ == "__main__":
    main()

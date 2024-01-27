import streamlit as st

from questions import post_match_form
from utils.auth import is_user_logged_in, login_page, logout
from utils.config import get_language
from utils.fmt import br, h1
from utils.translation import Translation

st.set_page_config(
    page_title="Método Avanza",
    page_icon="static/img/logo_avanza.webp",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Step 1: Create a Streamlit app with a login page
def main():
    tl = Translation("es") # default language is Spanish
    lang: str = get_language(tl) # get the language from the session state
    tl: Translation = Translation(lang) # refresh the translation obj with the lang from the session state
    
    
    # Show image logo at static/img/logo_avanza.webp
    _, logo_col, _ = st.columns([5, 4, 5])

    with logo_col:
        st.image("static/img/logo_avanza.webp", output_format="png")
    
    # Language selection
    if is_user_logged_in():
        with st.sidebar:
            tl.select_language()
            br(1)
            if st.button(tl.LOGOUT_BUTTON):
                logout()
    else:
        tl.select_language()

    # Login page
    if not is_user_logged_in():
        login_page(tl=tl)

    else:
        h1(tl.QUESTIONNAIRE_TITLE)
        post_match_form(tl)
                
if __name__ == "__main__":
    main()

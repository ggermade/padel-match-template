import streamlit as st

from home import home_page
from questions import post_match_form
from utils.auth import is_user_logged_in, login_page, logout
from utils.config import get_language
from utils.forms import get_form
from utils.logo import set_logo
from utils.translation import Form, Translation

st.set_page_config(
    page_title="Método Avanza",
    page_icon="static/img/logo_avanza.webp",
    layout="centered",
    initial_sidebar_state="expanded",
)

lang: str = get_language(tl=Translation("es")) # get the language from the session state, default to "es"
tl: Translation = Translation(lang) # refresh the translation obj with the lang from the session state

# Show image logo at static/img/logo_avanza.webp
set_logo()

# Language selection
if not is_user_logged_in():
    tl.select_language()
    login_page(tl=tl)
    
else:
    page_name_to_funcs = {
        tl.HOME: home_page,
        tl.QUESTIONNAIRE_TITLE: post_match_form,
        tl.LESSON_1_1_TITLE: get_form("lesson_1_1"),
        tl.LESSON_1_2_TITLE: get_form("lesson_1_2"),
        tl.LESSON_1_3_TITLE: get_form("lesson_1_3"),
    }

    with st.sidebar:
        if st.button(tl.LOGOUT_BUTTON):
            logout()
        tl.select_language()
        page_selection = st.radio(tl.MENU, list(page_name_to_funcs.keys()))
        

    if page_selection in [tl.HOME, tl.QUESTIONNAIRE_TITLE]:
        page_name_to_funcs[page_selection](tl=tl)
    else:
        form: Form = page_name_to_funcs[page_selection](tl=tl)
        form.render()

        
    
    

    

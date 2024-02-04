import streamlit as st

from forms import form_to_funcs
from home import home_page
from questions import post_match_form
from utils.auth import is_user_logged_in, login_page, logout
from utils.config import get_language
from utils.fmt import hr
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
    with st.sidebar:
        # Logout button
        if st.button(tl.LOGOUT_BUTTON):
            logout()

        # Select language
        tl.select_language()

        # Navigation
        form_selection = None
        page_selection = st.selectbox(tl.NAVIGATION, [tl.NAV_FORMS, tl.NAV_BIG_FORM, tl.NAV_HISTORY, tl.NAV_ANALYTICS])
        hr()

        if page_selection == tl.NAV_FORMS:
            form_func_map = form_to_funcs(tl=tl)
            form_selection = st.radio(tl.MENU, list(form_func_map.keys()))      
        elif page_selection == tl.NAV_HISTORY:
            st.write(tl.NAV_HISTORY)
        elif page_selection == tl.NAV_ANALYTICS:
            st.write(tl.NAV_ANALYTICS)
        elif page_selection == tl.NAV_BIG_FORM:
            pass
        
    if page_selection == tl.NAV_FORMS:

        if form_selection == tl.HOME:
            home_page(tl=tl)
        elif form_selection in form_func_map.keys():
            form: Form = form_func_map[form_selection](tl=tl)
            form.render()

    elif page_selection == tl.NAV_BIG_FORM:
        post_match_form(tl=tl)

        
    
    

    

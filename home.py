import streamlit as st

from utils.fmt import h2
from utils.translation import Translation


def home_page(tl: Translation):
    h2(tl.HOME_TITLE, align="left")
    st.markdown(tl.HOME_DESCRIPTION)
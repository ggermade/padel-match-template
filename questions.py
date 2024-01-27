import enum

import streamlit as st

from utils.fmt import h3, hr
from utils.translation import Translation


class ContextType(enum.Enum):
    DATA_COLLECTION = "data"
    PRE_MATCH = "pre_match"
    PHYSICAL = "physical"
    MENTAL_EMOTIONAL = "mental_emotional"
    TECHNICAL_TACTICAL_STRATEGIC = "technical_tactical_strategic"


class Question:
    def __init__(
        self,
        question_text: str,
        context: ContextType,
        st_widget: callable,
        *args,
        **kwargs,
    ):
        self._widget = st_widget
        self._text = question_text
        self._context = context
        self._args = args
        self._kwargs = kwargs

    def ask(self):
        return self._widget(label=self._text, *self._args, **self._kwargs)


physical_questions = []
mental_emotional_questions = []
technical_questions = []


# Step 5: Display the questionnaire to the user
def post_match_form(tl: Translation):
    with st.form(key="post-match-form"):
        
        h3(tl.DATA_COLLECTION_TITLE)
        data_collection_questions(tl)
        hr()
        h3(tl.PRE_MATCH_TITLE)
        pre_match_questions(tl)
        hr()
        h3(tl.PHYSICAL_TITLE)
        physical_questions(tl)
        hr()
        h3(tl.MENTAL_EMOTIONAL_TITLE)
        mental_emotional_questions(tl)
        hr()
        h3(tl.TECHNICAL_TACTICAL_STRATEGIC_TITLE)
        technical_questions(tl)

        if st.form_submit_button(tl.SUBMIT_BUTTON):
                # todo: save the user's responses to a database or file
                st.success(tl.SUBMIT_SUCCESS)
                st.balloons()


def data_collection_questions(tl: Translation):
    col1, col2 = st.columns(2)

    with col1:
        Question(tl.MATCH_DATE, ContextType.DATA_COLLECTION.value, st.date_input).ask()
        Question(
            question_text=tl.RESULT,
            context=ContextType.DATA_COLLECTION.value,
            st_widget=st.selectbox,
            options=tl.RESULT_OPTIONS,
        ).ask()

    with col2:
        Question(tl.OPPONENT_1, ContextType.DATA_COLLECTION.value, st.text_input).ask()
        Question(tl.OPPONENT_2, ContextType.DATA_COLLECTION.value, st.text_input).ask()

def pre_match_questions(tl: Translation):
    st.write(tl.PRE_MATCH_1)
    st.radio("", options=tl.PRE_MATCH_1_OPTIONS, key="pre_match_1", horizontal=True, label_visibility="collapsed")
    
    st.write(tl.PRE_MATCH_2)
    st.radio("", tl.PRE_MATCH_2_OPTIONS, key="pre_match_2", horizontal=True, label_visibility="collapsed")
    
    st.write(tl.PRE_MATCH_3)
    st.radio("", tl.PRE_MATCH_3_OPTIONS, key="pre_match_3", horizontal=True, label_visibility="collapsed")
    st.text_area(tl.PRE_MATCH_3_TEXT, key="pre_match_3_text", height=0, max_chars=1000, value="")

    st.write(tl.PRE_MATCH_4)
    st.radio("", tl.PRE_MATCH_4_OPTIONS, key="pre_match_4", horizontal=True, label_visibility="collapsed")
    
    st.write(tl.PRE_MATCH_5)
    st.text_area("", key="pre_match_5", height=0, max_chars=1000, value="", label_visibility="collapsed")

    st.write(tl.PRE_MATCH_6)
    st.radio("", tl.PRE_MATCH_6_OPTIONS, key="pre_match_6", horizontal=True, label_visibility="collapsed")


def physical_questions(tl: Translation):
    st.write(tl.PHYSICAL_1)
    st.text_area("", key="physical_1", height=0, max_chars=1000, value="", label_visibility="collapsed")

    st.write(tl.PHYSICAL_2)
    st.radio("", tl.PHYSICAL_2_OPTIONS, key="physical_2", horizontal=True, label_visibility="collapsed")

    st.write(tl.PHYSICAL_3)
    st.radio("", tl.PHYSICAL_3_OPTIONS, key="physical_3", horizontal=True, label_visibility="collapsed")

    st.write(tl.PHYSICAL_4)
    st.radio("", tl.PHYSICAL_4_OPTIONS, key="physical_4", horizontal=True, label_visibility="collapsed")

    st.write(tl.PHYSICAL_5)
    st.text_area("", key="physical_5", height=0, max_chars=1000, value="", label_visibility="collapsed")

def mental_emotional_questions(tl: Translation):
    st.write(tl.MENTAL_1)
    st.radio("", tl.MENTAL_1_OPTIONS, key="mental_emotional_1", horizontal=True, label_visibility="collapsed")

    st.write(tl.MENTAL_2)
    st.radio("", tl.MENTAL_2_OPTIONS, key="mental_emotional_2", horizontal=True, label_visibility="collapsed")

    st.write(tl.MENTAL_3)
    st.radio("", tl.MENTAL_3_OPTIONS, key="mental_emotional_3", horizontal=True, label_visibility="collapsed")

    st.write(tl.MENTAL_4)
    st.text_area("", key="mental_emotional_4", height=0, max_chars=1000, value="", label_visibility="collapsed")

    st.write(tl.MENTAL_5)
    st.radio("", tl.MENTAL_5_OPTIONS, key="mental_emotional_5", horizontal=True, label_visibility="collapsed")

    st.write(tl.MENTAL_6)
    st.text_area("", key="mental_emotional_6", height=0, max_chars=1000, value="", label_visibility="collapsed")

    st.write(tl.MENTAL_7)
    st.text_area("", key="mental_emotional_7", height=0, max_chars=1000, value="", label_visibility="collapsed")

    st.write(tl.MENTAL_8)
    st.text_area("", key="mental_emotional_8", height=0, max_chars=1000, value="", label_visibility="collapsed")

    st.write(tl.MENTAL_9)
    st.text_area("", key="mental_emotional_9", height=0, max_chars=1000, value="", label_visibility="collapsed")


def technical_questions(tl: Translation):
    st.write(tl.TECHNICAL_1)
    st.radio("", tl.TECHNICAL_1_OPTIONS, key="technical_1", horizontal=True, label_visibility="collapsed")

    st.write(tl.TECHNICAL_2)
    st.radio("", tl.TECHNICAL_2_OPTIONS, key="technical_2", horizontal=True, label_visibility="collapsed")

    st.write(tl.TECHNICAL_3)
    st.radio("", tl.TECHNICAL_3_OPTIONS, key="technical_3", horizontal=True, label_visibility="collapsed")

    st.write(tl.TECHNICAL_4)
    st.radio("", tl.TECHNICAL_4_OPTIONS, key="technical_4", horizontal=True, label_visibility="collapsed")

    st.write(tl.TECHNICAL_5)
    st.radio("", tl.TECHNICAL_5_OPTIONS, key="technical_5", horizontal=True, label_visibility="collapsed")

    st.write(tl.TECHNICAL_6)
    st.radio("", tl.TECHNICAL_6_OPTIONS, key="technical_6", horizontal=True, label_visibility="collapsed")

    st.write(tl.TECHNICAL_7)
    st.radio("", tl.TECHNICAL_7_OPTIONS, key="technical_7", horizontal=True, label_visibility="collapsed")

    st.write(tl.TECHNICAL_8)
    st.radio("", tl.TECHNICAL_8_OPTIONS, key="technical_8", horizontal=True, label_visibility="collapsed")

    st.write(tl.TECHNICAL_9)
    st.slider("", min_value=0, max_value=5, value=0, key="technical_9", label_visibility="collapsed")

    st.write(tl.TECHNICAL_10)
    st.radio("", tl.TECHNICAL_10_OPTIONS, key="technical_10", horizontal=True, label_visibility="collapsed")

    st.write(tl.TECHNICAL_11)
    st.radio("", tl.TECHNICAL_11_OPTIONS, key="technical_11", horizontal=True, label_visibility="collapsed")

    st.write(tl.TECHNICAL_12)
    st.radio("", tl.TECHNICAL_12_OPTIONS, key="technical_12", horizontal=True, label_visibility="collapsed")

    st.write(tl.TECHNICAL_13)
    st.text_area("", key="technical_13", height=0, max_chars=1000, value="", label_visibility="collapsed")

    st.write(tl.TECHNICAL_14)
    st.text_area("", key="technical_14", height=0, max_chars=1000, value="", label_visibility="collapsed")

    st.write(tl.TECHNICAL_15)
    st.text_area("", key="technical_15", height=0, max_chars=1000, value="", label_visibility="collapsed")




# Step 7: Implement feature to view previous responses
def show_previous_responses():
    # Retrieve and display the user's previous responses from the database or file
    pass


def show_settings(tl: Translation):
    st.header(tl.SETTINGS_TITLE)
    st.write(tl.SETTINGS_LANGUAGE)
    st.selectbox(tl.SETTINGS_LANGUAGE_OPTIONS)

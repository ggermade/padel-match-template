import enum

import streamlit as st

from utils.fmt import hr
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
        
        st.subheader(tl.DATA_COLLECTION_TITLE)
        data_collection_questions(tl)
        hr()
        st.subheader(tl.PHYSICAL_TITLE)
        # context_map[ContextType.PHYSICAL](tl)
        hr()
        st.subheader(tl.MENTAL_EMOTIONAL_TITLE)
        # context_map[ContextType.MENTAL_EMOTIONAL](tl)
        hr()
        st.subheader(tl.TECHNICAL_TACTICAL_STRATEGIC_TITLE)
        # context_map[ContextType.TECHNICAL_TACTICAL_STRATEGIC](tl)

        if st.form_submit_button(tl.SUBMIT_BUTTON):
                # todo: save the user's responses to a database or file
                st.success(tl.SUBMIT_SUCCESS)
                st.balloons()


def data_collection_questions(translation: Translation):
    QT = translation.QuestionText
    col1, col2 = st.columns(2)

    with col1:
        Question(QT.MATCH_DATE, ContextType.DATA_COLLECTION.value, st.date_input).ask()
        Question(
            question_text=QT.RESULT,
            context=ContextType.DATA_COLLECTION.value,
            st_widget=st.selectbox,
            options=QT.RESULT_OPTIONS,
        ).ask()

    with col2:
        Question(QT.OPPONENT_1, ContextType.DATA_COLLECTION.value, st.text_input).ask()
        Question(QT.OPPONENT_2, ContextType.DATA_COLLECTION.value, st.text_input).ask()
    
def physical_questions(translation: Translation):
    QT = translation.QuestionText
    col1, col2 = st.columns(2)

    with col1:
        Question(QT.MATCH_DATE, ContextType.DATA_COLLECTION.value, st.date_input).ask()
        Question(
            question_text=QT.RESULT,
            context=ContextType.DATA_COLLECTION.value,
            st_widget=st.selectbox,
            options=QT.RESULT_OPTIONS,
        ).ask()

    with col2:
        Question(QT.OPPONENT_1, ContextType.DATA_COLLECTION.value, st.text_input).ask()
        Question(QT.OPPONENT_2, ContextType.DATA_COLLECTION.value, st.text_input).ask()

def mental_emotional_questions(translation: Translation):
    pass

def technical_questions(translation: Translation):
    pass


# Step 7: Implement feature to view previous responses
def show_previous_responses():
    # Retrieve and display the user's previous responses from the database or file
    pass


def show_settings(tl: Translation):
    st.header(tl.SETTINGS_TITLE)
    st.write(tl.SETTINGS_LANGUAGE)
    st.selectbox(tl.SETTINGS_LANGUAGE_OPTIONS)

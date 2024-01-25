
import streamlit as st

from utils import translation as tl
from utils.config import get_language

language = get_language()

# class ContextType(enum.Enum):
#     DATA_COLLECTION = "data"
#     PRE_MATCH = "pre_match"
#     PHYSICAL = "physical"
#     MENTAL_EMOTIONAL = "mental_emotional"
#     TECHNICAL_TACTICAL_STRATEGIC = "technical_tactical_strategic"


class Question:
    def __init__(self, question_text: str, st_widget: callable, *args, **kwargs):
        self._widget = st_widget
        self._text = question_text
        self._args = args
        self._kwargs = kwargs

    def ask(self):
        return self._widget(self._text, *self._args, **self._kwargs)
    
# I don't want to read from the file anymore, I'd rather write the questions in code
data_entry_questions = {
    "es": [
        Question("Fecha del partido", st.date_input),
        Question("Nombre Rival 1", st.text_input),
        Question("Nombre Rival 2", st.text_input),
        Question("Resultado", st.radio, options=["Victoria", "Empate", "Derrota", "Incompleto"], horizontal=True),
    ],
    "en": [
        Question("Match date", st.date_input),
        Question("Opponent 1", st.text_input),
        Question("Opponent 2", st.text_input),
        Question("Result", st.radio, options=["Win", "Draw", "Loss", "Incomplete"], horizontal=True),
    ]
}

    

# Step 5: Display the questionnaire to the user
def show_questionnaire():
    
    st.header(tl.QUESTIONNAIRE_TITLE)
    
    for question in data_entry_questions[language]:
        question.ask()
        
    st.button(tl.SUBMIT_BUTTON)

# Step 7: Implement feature to view previous responses
def show_previous_responses():
    # Retrieve and display the user's previous responses from the database or file
    pass
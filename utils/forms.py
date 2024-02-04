import streamlit as st

from .translation import Form, Translation


def get_form(form_name: str) -> Form:
    form_name_to_class = {
        "lesson_1_1": Lesson1_1,
        "lesson_1_2": Lesson1_2,
        "lesson_1_3": Lesson1_3,
    }
    return form_name_to_class[form_name]

class Lesson1_1(Form):

    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": "Lección 1.1: La Consistencia",
            "en": "Lesson 1.1: Consistency",
        }[self.tl.lang]
        self.root_key = "lesson_1_1"
        self.set_specific_questions()
    
    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Cuántos errores no forzados has tenido en todo el partido?",
            "en": "How many unforced errors did you make throughout the whole match?",
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿En qué momentos del partido has fallado más?",
            "en": "In which moments of the match did you miss the most?",
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Crees que al estar pendiente de los errores, has fallado menos que en tus partidos anteriores?",
            "en": "Do you think you missed fewer shots than in your previous matches by being mindful of your errors?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": ["Sí", "No", "No estoy seguro/a"],
            "en": ["Yes", "No", "I'm not so sure"],
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "¿Te frustras cuando cometes errores? Si lo haces, ¿qué haces para cambiarlo?",
            "en": "Do you get frustrated when you make mistakes? If you do, what do you do to handle it?",
        }[self.tl.lang]

    def render_specific_questions(self):
        st.write(self.QUESTION_1)
        st.number_input("", min_value=0, max_value=100, value=0, step=1, key=f"{self.root_key}_1")
        st.write(self.QUESTION_2)
        st.text_area("", key=f"{self.root_key}_2", height=0, max_chars=1000, label_visibility="collapsed")
        st.write(self.QUESTION_3)
        st.radio("", options=self.QUESTION_3_OPTIONS, key=f"{self.root_key}_3", horizontal=True, label_visibility="collapsed")
        st.write(self.QUESTION_4)
        st.text_area("", key=f"{self.root_key}_4", height=0, max_chars=1000, label_visibility="collapsed")

class Lesson1_2(Form):
    
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": "Lección 1.2: La Concentración",
            "en": "Lesson 1.2: Concentration",
        }[self.tl.lang]
        self.root_key = "lesson_1_2"
        self.set_specific_questions()
    
    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Cómo ha ido hoy tu consistencia? ¿Has fallado más o menos que el partido anterior?",
            "en": "How was your consistency today? Did you make more or less unforced errors than the previous match?",
        }[self.tl.lang]

        self.QUESTION_1_OPTIONS = {
            "es": ["Más errores", "Menos errores", "Más o menos igual"],
            "en": ["More errors", "Less errors", "More or less the same"],
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Has conseguido ganar la red más veces que tus contrarios?",
            "en": "Have you managed to win the net more times than your opponents?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": ["Sí", "No", "No estoy seguro/a"],
            "en": ["Yes", "No", "I'm not sure"],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "Cuándo has ganado la red, ¿has conseguido mantenerte en ella, o pierdes la red fácilmente?",
            "en": "Once you had won the net, did you manage to keep the net position, or did you lose it quickly?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": ["Me mantengo", "Pierdo la red fácilmente", "No estoy seguro/a"],
            "en": ["I keep it", "I lose the net easily", "I'm not sure"],
        }[self.tl.lang]

    def render_specific_questions(self):
        st.write(self.QUESTION_1)
        st.radio("", options=self.QUESTION_1_OPTIONS, key=f"{self.root_key}_1", horizontal=True, label_visibility="collapsed")
        st.write(self.QUESTION_2)
        st.radio("", options=self.QUESTION_2_OPTIONS, key=f"{self.root_key}_2", horizontal=True, label_visibility="collapsed")
        st.write(self.QUESTION_3)
        st.radio("", options=self.QUESTION_3_OPTIONS, key=f"{self.root_key}_3", horizontal=True, label_visibility="collapsed")

class Lesson1_3(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": "Lección 1.3: Bolas Fáciles o Difíciles en la Defensa",
            "en": "Lesson 1.3: Easy or Difficult Balls in the Defense",
        }[self.tl.lang]
        self.root_key = "lesson_1_3"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Te ha resultado fácil distinguir las bolas fáciles o difíciles?",
            "en": "Did you find it easy to distinguish between easy and difficult balls?",
        }[self.tl.lang]

        self.QUESTION_1_OPTIONS = {
            "es": ["Sí", "No", "A veces sí, a veces no"],
            "en": ["Yes", "No", "Sometimes yes, sometimes no"],
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Has jugado rápido y por abajo las bolas difíciles? ¿Has metido más de las que has fallado o al revés?",
            "en": "Have you played fast and low on difficult balls? Have you put the ball in more than you have missed, or was it the other way around?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": ["Sí jugué rápido y por abajo, y metí más de las que fallé", "Sí jugué rápido y por abajo, pero fallé más de las que metí", "No pude conseguir jugar rápido y por abajo"],
            "en": ["Yes, I played fast and low, and I put in more than I missed", "Yes, I played fast and low, but I missed more than I put in", "I couldn't manage to play fast and low"],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "Si has conseguido jugar rápido por abajo, ¿qué efecto ha provocado en los rivales y en la bola de vuelta?",
            "en": "If you managed to play fast and low, what effect did it have on the opponents and the balls they returned in response?",
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "Con la bola más fácil, ¿has conseguido ganar la red?. Cuéntanos cómo te ha ido con ambas bolas.",
            "en": "With the easier ball, did you manage to win the net? Tell us how you did with both ball types.",
        }[self.tl.lang]

    def render_specific_questions(self):
        st.write(self.QUESTION_1)
        st.radio("", options=self.QUESTION_1_OPTIONS, key=f"{self.root_key}_1", horizontal=True, label_visibility="collapsed")
        st.write(self.QUESTION_2)
        st.radio("", options=self.QUESTION_2_OPTIONS, key=f"{self.root_key}_2", horizontal=False, label_visibility="collapsed")
        st.write(self.QUESTION_3)
        st.text_area("", key=f"{self.root_key}_3", height=0, max_chars=1000, label_visibility="collapsed")
        st.write(self.QUESTION_4)
        st.text_area("", key=f"{self.root_key}_4", height=0, max_chars=1000, label_visibility="collapsed")
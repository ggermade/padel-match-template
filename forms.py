import streamlit as st

from home import home_page
from utils.fmt import h6
from utils.translation import Form, Translation


def get_form(form_name: str) -> Form:
    form_name_to_class = {
        "lesson_1_1": Lesson1_1,
        "lesson_1_2": Lesson1_2,
        "lesson_1_3": Lesson1_3,
        "lesson_2_1": Lesson2_1,
        "lesson_2_2": Lesson2_2,
        "lesson_2_3": Lesson2_3,
        "lesson_2_4": Lesson2_4,
        "lesson_3_1": Lesson3_1,
        "lesson_3_2": Lesson3_2,
        "lesson_3_3": Lesson3_3,
        "lesson_4_1": Lesson4_1,
        "lesson_4_2": Lesson4_2,
        "lesson_4_3": Lesson4_3,
        "lesson_5_1": Lesson5_1,
        "lesson_5_2": Lesson5_2,
        "lesson_5_3": Lesson5_3,
        "lesson_6_1": Lesson6_1,
        "lesson_6_2": Lesson6_2,
    }
    return form_name_to_class.get(form_name, Form)


def form_to_funcs(tl: Translation) -> dict:
    return {
        tl.HOME: home_page,
        tl.LESSON_1_1_TITLE: get_form("lesson_1_1"),
        tl.LESSON_1_2_TITLE: get_form("lesson_1_2"),
        tl.LESSON_1_3_TITLE: get_form("lesson_1_3"),
        tl.LESSON_2_1_TITLE: get_form("lesson_2_1"),
        tl.LESSON_2_2_TITLE: get_form("lesson_2_2"),
        tl.LESSON_2_3_TITLE: get_form("lesson_2_3"),
        tl.LESSON_2_4_TITLE: get_form("lesson_2_4"),
        tl.LESSON_3_1_TITLE: get_form("lesson_3_1"),
        tl.LESSON_3_2_TITLE: get_form("lesson_3_2"),
        tl.LESSON_3_3_TITLE: get_form("lesson_3_3"),
        tl.LESSON_4_1_TITLE: get_form("lesson_4_1"),
        tl.LESSON_4_2_TITLE: get_form("lesson_4_2"),
        tl.LESSON_4_3_TITLE: get_form("lesson_4_3"),
        tl.LESSON_5_1_TITLE: get_form("lesson_5_1"),
        tl.LESSON_5_2_TITLE: get_form("lesson_5_2"),
        tl.LESSON_5_3_TITLE: get_form("lesson_5_3"),
        tl.LESSON_6_1_TITLE: get_form("lesson_6_1"),
        tl.LESSON_6_2_TITLE: get_form("lesson_6_2"),
    }


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
        h6(self.QUESTION_1)
        st.number_input(
            label="",
            min_value=0,
            max_value=100,
            value=0,
            step=1,
            key=f"{self.root_key}_1",
        )
        h6(self.QUESTION_2)
        st.text_area(
            label="",
            key=f"{self.root_key}_2",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.radio(
            label="",
            options=self.QUESTION_3_OPTIONS,
            key=f"{self.root_key}_3",
            horizontal=True,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_4)
        st.text_area(
            label="",
            key=f"{self.root_key}_4",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )


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
        h6(self.QUESTION_1)
        st.radio(
            label="",
            options=self.QUESTION_1_OPTIONS,
            key=f"{self.root_key}_1",
            horizontal=True,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.radio(
            label="",
            options=self.QUESTION_2_OPTIONS,
            key=f"{self.root_key}_2",
            horizontal=True,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.radio(
            label="",
            options=self.QUESTION_3_OPTIONS,
            key=f"{self.root_key}_3",
            horizontal=True,
            label_visibility="collapsed",
        )


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
            "es": [
                "Sí jugué rápido y por abajo, y metí más de las que fallé",
                "Sí jugué rápido y por abajo, pero fallé más de las que metí",
                "No pude conseguir jugar rápido y por abajo",
            ],
            "en": [
                "Yes, I played fast and low, and I put in more than I missed",
                "Yes, I played fast and low, but I missed more than I put in",
                "I couldn't manage to play fast and low",
            ],
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
        h6(self.QUESTION_1)
        st.radio(
            label="",
            options=self.QUESTION_1_OPTIONS,
            key=f"{self.root_key}_1",
            horizontal=True,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.radio(
            label="",
            options=self.QUESTION_2_OPTIONS,
            key=f"{self.root_key}_2",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.text_area(
            label="",
            key=f"{self.root_key}_3",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_4)
        st.text_area(
            label="",
            key=f"{self.root_key}_4",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )


class Lesson2_1(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": f"Lección {tl.LESSON_2_1_TITLE}",
            "en": f"Lesson {tl.LESSON_2_1_TITLE}",
        }[self.tl.lang]
        self.root_key = "lesson_2_1"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Qué tal ha ido el primer set ganando tiempo?",
            "en": "How did it go in the first set, when you were buying time?",
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Cómo fue quitar tiempo en el segundo set?",
            "en": "What was it like to take time away from your opponents during the second set?",
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "Cuéntanos qué te ha resultado más fácil, qué te ha costado más, a qué velocidad te gusta más jugar.",
            "en": "Tell us which strategy was easier and which more difficult, at what speed do you like to play the most?",
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "¿Has detectado qué velocidad le ha incomodado más a tus rivales?",
            "en": "Have you identified which speed bothered your opponents the most?",
        }[self.tl.lang]

        self.QUESTION_4_OPTIONS = {
            "es": [
                "Sí, les incomodó más la velocidad alta",
                "Sí, les incomodó más la velocidad baja",
                "Creo que se manejaban bien con ambas velocidades",
                "No llegué a decifrar qué velocidad les incomodó más",
            ],
            "en": [
                "Yes, they were more bothered by fast-paced play",
                "Yes, they were more bothered by slow-paced play",
                "I think they handled both speeds well",
                "I didn't manage to figure out which speed bothered them the most",
            ],
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.text_area(
            label="",
            key=f"{self.root_key}_1",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.text_area(
            label="",
            key=f"{self.root_key}_2",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.text_area(
            label="",
            key=f"{self.root_key}_3",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_4)
        st.radio(
            label="",
            options=self.QUESTION_4_OPTIONS,
            key=f"{self.root_key}_4",
            horizontal=False,
            label_visibility="collapsed",
        )


class Lesson2_2(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": f"Lección {tl.LESSON_2_2_TITLE}",
            "en": f"Lesson {tl.LESSON_2_2_TITLE}",
        }[self.tl.lang]
        self.root_key = "lesson_2_2"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Has conseguido distinguir los espacios por delante y por detrás del rival?",
            "en": "Were you able to identify spaces in front of and behind the opponent?",
        }[self.tl.lang]

        self.QUESTION_1_OPTIONS = {
            "es": [
                "Sí, los distinguí",
                "No, no los pude distinguir",
                "Más o menos, tengo dudas",
            ],
            "en": [
                "Yes, I identified them",
                "No, I didn't identify them",
                "I'm not so sure, I have doubts",
            ],
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Has logrado jugar a esos espacios?",
            "en": "Were you able to play to the spaces?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": [
                "Sí, logré jugar a los espacios",
                "No, no logré jugar a los espacios",
                "No logré hacerlo consistentemente",
            ],
            "en": [
                "Yes, I managed to play to the spaces",
                "No, I didn't manage to play to the spaces",
                "I didn't manage to do it consistently",
            ],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Has conseguido desplazarlos hacia atrás y hacia delante?",
            "en": "Did you manage to make your opponents run back and forth?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": [
                "Sí, los desplacé hacia atrás y hacia delante",
                "No, no logré desplazarlos",
                "No logré hacerlo consistentemente",
            ],
            "en": [
                "Yes, I made them run back and forth",
                "No, I didn't manage to make them run back and forth",
                "I didn't manage to do it consistently",
            ],
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "Cuéntanos qué te ha resultado más fácil o más difícil del objetivo de hoy.",
            "en": "Tell us what you found the easiest or the most difficult about today's objective.",
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.radio(
            label="",
            options=self.QUESTION_1_OPTIONS,
            key=f"{self.root_key}_1",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.radio(
            label="",
            options=self.QUESTION_2_OPTIONS,
            key=f"{self.root_key}_2",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.radio(
            label="",
            options=self.QUESTION_3_OPTIONS,
            key=f"{self.root_key}_3",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_4)
        st.text_area(
            label="",
            key=f"{self.root_key}_4",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )


class Lesson2_3(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": f"Lección {tl.LESSON_2_3_TITLE}",
            "en": f"Lesson {tl.LESSON_2_3_TITLE}",
        }[self.tl.lang]
        self.root_key = "lesson_2_3"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Has conseguido preparar pronto tus golpes de fondo?",
            "en": "Have you managed to prepare early for your groundstrokes?",
        }[self.tl.lang]

        self.QUESTION_1_OPTIONS = {
            "es": [
                "Sí, los preparé pronto o más pronto que antes",
                "No, no los preparé pronto, sentí que me faltaba tiempo",
                "No logré hacerlo consistentemente, en ocasiones sí, en ocasiones no",
            ],
            "en": [
                "Yes, I prepared them early or earlier than before",
                "No, I didn't prepare them early, I felt I lacked time to do it well",
                "I didn't manage to do it consistently, sometimes yes, sometimes not",
            ],
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Has utilizado la misma preparación para tu golpe de derecha? ¿y de revés?",
            "en": "Have you managed to achieve a consistent, repetitive motion for your forehand? What about your backhand?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": [
                "Logré ser consistente en la preparación de ambos golpes",
                "Logré ser consistente en el golpe de derecha, pero no en el de revés",
                "Logré ser consistente en el golpe de revés, pero no en el de derecha",
                "No logré ser consistente en la preparación de ninguno de los dos golpes",
            ],
            "en": [
                "I managed to be consistent in the preparation of both shots",
                "I managed to be consistent in the forehand, but not in the backhand",
                "I managed to be consistent in the backhand, but not in the forehand",
                "I didn't manage to be consistent in the preparation of either shot",
            ],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Has llegado al objetivo de engañar a tus rivales?",
            "en": "Have you reached the goal of deceiving your rivals?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": [
                "Sí, logré engañar a mis rivales",
                "No, no logré engañar a mis rivales",
                "Logré hacerlo una o dos veces solamente",
            ],
            "en": [
                "Yes, I managed to deceive my opponents",
                "No, I didn't manage to deceive my opponents",
                "I only managed to do it once or twice",
            ],
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.radio(
            label="",
            options=self.QUESTION_1_OPTIONS,
            key=f"{self.root_key}_1",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.radio(
            label="",
            options=self.QUESTION_2_OPTIONS,
            key=f"{self.root_key}_2",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.radio(
            label="",
            options=self.QUESTION_3_OPTIONS,
            key=f"{self.root_key}_3",
            horizontal=False,
            label_visibility="collapsed",
        )


class Lesson2_4(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": f"Lección {tl.LESSON_2_4_TITLE}",
            "en": f"Lesson {tl.LESSON_2_4_TITLE}",
        }[self.tl.lang]
        self.root_key = "lesson_2_4"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "Dinos cómo ha ido el peloteo.",
            "en": "Tell us how the warm-up rally went.",
        }[self.tl.lang]

        self.QUESTION_1_OPTIONS = {
            "es": [
                "Muy bien, logré enfocarme en el objetivo desde el inicio e hice pocos errores",
                "Bien, logré enfocarme en el objetivo desde el inicio, pero cometí más errores de los que me hubiera gustado",
                "Regular, no logré enfocarme en el objetivo desde el inicio y cometí más errores de los que me hubiera gustado",
                "Mal, no logré enfocarme en el objetivo desde el inicio y cometí muchos errores",
            ],
            "en": [
                "Very well, I managed to focus on the goal from the start and made few mistakes",
                "Good, I managed to focus on the goal from the start, but made more mistakes than I would have liked",
                "Regular, I didn't manage to focus on the goal from the start and made more mistakes than I would have liked",
                "Bad, I didn't manage to focus on the goal from the start and made many mistakes",
            ],
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Has conseguido jugar a las zonas más incómodas para tu rival?",
            "en": "Did you manage to play to the most uncomfortable areas for your opponent?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": [
                "Sí, logré jugar a las zonas más incómodas",
                "No, no logré jugar a las zonas más incómodas",
                "No logré hacerlo consistentemente",
            ],
            "en": [
                "Yes, I managed to play to the most uncomfortable areas",
                "No, I didn't manage to play to the most uncomfortable areas",
                "I didn't manage to do it consistently",
            ],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Qué zona te ha resultado más difícil? ¿Cuál te ha dado mejor resultado?",
            "en": "Which area has been the most difficult for you to target? Which area has given you the best results?",
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "¿Te ha parecido que jugando a esas zonas neutralizabas a tus rivales?",
            "en": "Did it seem like playing to those areas neutralized your opponents' offensive capability?",
        }[self.tl.lang]

        self.QUESTION_4_OPTIONS = {
            "es": ["Sí", "No", "No logré hacerlo consistentemente para estar seguro/a"],
            "en": [
                "Yes",
                "No",
                "I didn't manage to do it consistently enough to be sure",
            ],
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.radio(
            label="",
            options=self.QUESTION_1_OPTIONS,
            key=f"{self.root_key}_1",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.radio(
            label="",
            options=self.QUESTION_2_OPTIONS,
            key=f"{self.root_key}_2",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.text_area(
            label="",
            key=f"{self.root_key}_3",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_4)
        st.radio(
            label="",
            options=self.QUESTION_4_OPTIONS,
            key=f"{self.root_key}_4",
            horizontal=False,
            label_visibility="collapsed",
        )


class Lesson3_1(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": f"Lección {tl.LESSON_3_1_TITLE}",
            "en": f"Lesson {tl.LESSON_3_1_TITLE}",
        }[self.tl.lang]
        self.root_key = "lesson_3_1"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Cómo te ha ido hoy al jugar el globo y subir a bloquear?",
            "en": "How did you do today playing the lob and going up to block?",
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Te has posicionado bien en el pico?",
            "en": "Have you positioned yourself well at the peak?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": [
                "Sí, me he posicionado bien",
                "No, no me he posicionado bien",
                "No logré hacerlo consistentemente",
            ],
            "en": [
                "Yes, I positioned myself well",
                "No, I didn't position myself well",
                "I didn't manage to do it consistently",
            ],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Consigues jugar el globo y dejar de mirar la bola y observar al jugador que golpea?",
            "en": "Did you manage to make the lob and watch the striking opponent's positioning instead of the ball?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": [
                "Sí, lo consigo",
                "No, no lo consigo",
                "No logré hacerlo consistentemente",
            ],
            "en": ["Yes", "No", "I didn't manage to do it consistently"],
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "¿Has conseguido bloquear hacia el jugador que golpea?",
            "en": "Have you managed to block towards the striking player?",
        }[self.tl.lang]

        self.QUESTION_4_OPTIONS = {
            "es": [
                "Sí, logré bloquear bien y hacia el jugador que golpea",
                "Sí logré bloquear, pero sin poder controlar la dirección",
                "No, no logré bloquear bien",
            ],
            "en": [
                "Yes, I managed to block well and towards the player who was striking",
                "Yes, I managed to block, but without being able to control the direction",
                "No, I didn't manage to block properly",
            ],
        }[self.tl.lang]

        self.QUESTION_5 = {
            "es": "¿Has sido capaz de bajar la velocidad en el bloqueo?",
            "en": "Have you been able to slow down the ball while blocking?",
        }[self.tl.lang]

        self.QUESTION_5_OPTIONS = {
            "es": [
                "Sí, logré bajar la velocidad",
                "No, no logré bajar la velocidad",
                "No logré hacerlo consistentemente",
            ],
            "en": [
                "Yes, I managed to lower the speed",
                "No, I didn't manage to lower the speed",
                "I didn't manage to do it consistently",
            ],
        }[self.tl.lang]

        self.QUESTION_6 = {
            "es": "¿Ha habido muchos errores? ¿Te has encontrado cómodo/a?",
            "en": "Did you make many mistakes? Did you feel comfortable?",
        }[self.tl.lang]

        self.QUESTION_6_OPTIONS = {
            "es": [
                "Sí, me he encontrado cómodo/a, sin hacer muchos errores",
                "No, no me he encontrado cómodo/a e hice muchos errores",
                "Más o menos cómodo/a, hice algunos errores",
            ],
            "en": [
                "Yes, I was comfortable, without making many mistakes",
                "No, I wasn't comfortable and made many mistakes",
                "More or less comfortable, I made some mistakes",
            ],
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.text_area(
            label="",
            key=f"{self.root_key}_1",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.radio(
            label="",
            options=self.QUESTION_2_OPTIONS,
            key=f"{self.root_key}_2",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.radio(
            label="",
            options=self.QUESTION_3_OPTIONS,
            key=f"{self.root_key}_3",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_4)
        st.radio(
            label="",
            options=self.QUESTION_4_OPTIONS,
            key=f"{self.root_key}_4",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_5)
        st.radio(
            label="",
            options=self.QUESTION_5_OPTIONS,
            key=f"{self.root_key}_5",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_6)
        st.radio(
            label="",
            options=self.QUESTION_6_OPTIONS,
            key=f"{self.root_key}_6",
            horizontal=False,
            label_visibility="collapsed",
        )


class Lesson3_2(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": f"Lección {tl.LESSON_3_2_TITLE}",
            "en": f"Lesson {tl.LESSON_3_2_TITLE}",
        }[self.tl.lang]
        self.root_key = "lesson_3_2"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Cómo te ha ido hoy al ganar la red?",
            "en": "How did it go today trying to win the net?",
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Has conseguido utilizar las tres opciones para ganar la red: volcada, globo que NO sobrepasa y globo que sobrepasa?",
            "en": "Did you manage to use all three options to win the net: chiquita, a lob that does NOT pass them, and a lob that does overtake them?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": [
                "Sí, las he utilizado todas",
                "Casi, me faltó sólo ganar la red con la volcada",
                "Casi, me faltó ganar la red con el globo que NO sobrepasa",
                "Casi, me faltó ganar la red con el globo que sobrepasa",
                "No, sólo logré ganar la red con una de las opciones (La volcada)",
                "No, sólo logré ganar la red con una de las opciones (El globo que NO sobrepasa)",
                "No, sólo logré ganar la red con una de las opciones (El globo que sobrepasa)",
            ],
            "en": [
                "Yes, I used them all",
                "Almost, I only missed winning the net with the chiquita",
                "Almost, I only missed winning the net with the lob that does NOT pass them",
                "Almost, I only missed winning the net with the lob that does overtake them",
                "No, I only managed to win the net with one of the options (The chiquita)",
                "No, I only managed to win the net with one of the options (The lob that does NOT pass them)",
                "No, I only managed to win the net with one of the options (The lob that does overtake them)",
            ],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Cuál te resulta más cómoda?",
            "en": "Which one did you find more comfortable?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": ["La volcada", "El globo que NO sobrepasa", "El globo que sobrepasa"],
            "en": [
                "The chiquita",
                "The lob that does NOT pass them",
                "The lob that does overtake them",
            ],
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "¿Cuál te cuesta más?",
            "en": "Which one did you find more difficult?",
        }[self.tl.lang]

        self.QUESTION_4_OPTIONS = {
            "es": ["La volcada", "El globo que NO sobrepasa", "El globo que sobrepasa"],
            "en": [
                "The chiquita",
                "The lob that does NOT pass them",
                "The lob that does overtake them",
            ],
        }[self.tl.lang]

        self.QUESTION_5 = {
            "es": "¿Cómo han sido tus bloqueos?",
            "en": "How have your blocks been?",
        }[self.tl.lang]

        self.QUESTION_6 = {
            "es": "¿Consigues estar tranquilo/a al bloquear o te aceleras al subir?",
            "en": "Do you manage to stay calm when blocking or do you get anxious when going up to block at the net?",
        }[self.tl.lang]

        self.QUESTION_6_OPTIONS = {
            "es": ["Sí, consigo estar tranquilo/a", "No, me acelero al subir"],
            "en": [
                "Yes, I manage to stay calm",
                "No, I get anxious when going up to block",
            ],
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.text_area(
            label="",
            key=f"{self.root_key}_1",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.radio(
            label="",
            options=self.QUESTION_2_OPTIONS,
            key=f"{self.root_key}_2",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.radio(
            label="",
            options=self.QUESTION_3_OPTIONS,
            key=f"{self.root_key}_3",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_4)
        st.radio(
            label="",
            options=self.QUESTION_4_OPTIONS,
            key=f"{self.root_key}_4",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_5)
        st.text_area(
            label="",
            key=f"{self.root_key}_5",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_6)
        st.radio(
            label="",
            options=self.QUESTION_6_OPTIONS,
            key=f"{self.root_key}_6",
            horizontal=False,
            label_visibility="collapsed",
        )


class Lesson3_3(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": f"Lección {tl.LESSON_3_3_TITLE}",
            "en": f"Lesson {tl.LESSON_3_3_TITLE}",
        }[self.tl.lang]
        self.root_key = "lesson_3_3"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Cómo te ha ido hoy en la transición a la red?",
            "en": "How did your transition to the net go today?",
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Has estado un poco más cómodo/a que en el partido anterior?",
            "en": "Were you a little more comfortable than in the previous match?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": [
                "Sí, me he sentido más cómodo/a",
                "Más o menos, me he sentido igual de cómodo/a",
                "No, me he sentido menos cómodo/a aún",
            ],
            "en": [
                "Yes, I felt more comfortable",
                "More or less, I felt equally comfortable",
                "No, I felt even less comfortable",
            ],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Has conseguido compenetrarte con tu compañero/a?",
            "en": "Have you been able to get along with your partner?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": [
                "Sí, me he compenetrado con mi compañero/a",
                "Neutral, me he compenetrado sólo un poco con mi compañero/a",
                "No, no me he comunicado mucho con mi compañero/a",
                "Me he llevado mal con mi compañero/a!",
            ],
            "en": [
                "Yes, I got along with my partner",
                "Neutral, I got along with my partner, but just a little",
                "No, I didn't communicate much with my partner",
                "I got along badly with my partner!",
            ],
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "¿Qué te ha resultado más fácil o difícil?",
            "en": "What has been easier or harder for you?",
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.text_area(
            label="",
            key=f"{self.root_key}_1",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.radio(
            label="",
            options=self.QUESTION_2_OPTIONS,
            key=f"{self.root_key}_2",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.radio(
            label="",
            options=self.QUESTION_3_OPTIONS,
            key=f"{self.root_key}_3",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_4)
        st.text_area(
            label="",
            key=f"{self.root_key}_4",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )


class Lesson4_1(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": f"Lección {tl.LESSON_4_1_TITLE}",
            "en": f"Lesson {tl.LESSON_4_1_TITLE}",
        }[self.tl.lang]
        self.root_key = "lesson_4_1"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Has conseguido estar en la red  más tiempo que tus rivales?",
            "en": "Have you managed to stay in the net longer than your rivals?",
        }[self.tl.lang]

        self.QUESTION_1_OPTIONS = {
            "es": [
                "Sí, he estado más tiempo en la red que mis rivales",
                "No, no he estado más tiempo en la red que mis rivales",
                "Creo que estuvimos igual de tiempo en la red que nuestros rivales",
            ],
            "en": [
                "Yes, I was at the net more than my opponents",
                "No, I wasn't at the net more than my opponents",
                "I think we were at the net around the same amount of time as our opponents",
            ],
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Has jugado voleas por delante y en dirección al jugador?",
            "en": "Have you played volleys in front of and in the direction of the players?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": [
                "Sí, he jugado voleas por delante y en dirección al jugador",
                "No, no he jugado voleas por delante y en dirección al jugador",
                "No logré hacerlo consistentemente",
            ],
            "en": [
                "Yes, I played volleys in front of and in the direction of the players",
                "No, I didn't play volleys in front of and in the direction of the players",
                "I didn't manage to do it consistently",
            ],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Qué te ha resultado más fácil? ¿En cruzado o en paralelo?",
            "en": "Which did you find easier, playing in cross court or parallel?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": [
                "En cruzado",
                "En paralelo",
                "Ambos me han resultado igual de fáciles",
                "Ambos me han resultado igual de difíciles",
            ],
            "en": [
                "Cross court",
                "Parallel",
                "Both were equally easy for me",
                "Both were equally difficult for me",
            ],
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "¿Perdíais la red con facilidad o conseguíais manteneros en ella?",
            "en": "Did you lose the net position easily or did you manage to stay in it?",
        }[self.tl.lang]

        self.QUESTION_4_OPTIONS = {
            "es": [
                "Me mantengo",
                "Pierdo la red fácilmente",
                "A veces logro mantenerme, a veces la pierdo fácilmente",
                "No estoy seguro/a",
            ],
            "en": [
                "I keep the net position",
                "I lose the net easily",
                "Sometimes I manage to keep it, sometimes I lose it easily",
                "I'm not sure",
            ],
        }[self.tl.lang]

        self.QUESTION_5 = {
            "es": "¿Habéis conseguido presionar y que os quede una bola clara para definir?",
            "en": "Did you manage to pressure and get a clear ball to finish the point?",
        }[self.tl.lang]

        self.QUESTION_5_OPTIONS = {
            "es": [
                "Sí, hemos conseguido presionar obtener bolas claras para definir, de manera consistente",
                "Sí, pero hemos sido inconsistentes, haciendo muchos errores",
                "Sí, pero hemos sido inconsistentes, perdiendo la red con facilidad",
                "No, no hemos conseguido presionar y obtener bolas claras para definir",
            ],
            "en": [
                "Yes, we managed to pressure and get clear balls to finish the point, consistently",
                "Yes, but we were inconsistent, making many mistakes while pressuring",
                "Yes, but we were inconsistent, losing the net position easily",
                "No, we didn't manage to pressure properly and get clear balls to finish the point",
            ],
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.radio(
            label="",
            options=self.QUESTION_1_OPTIONS,
            key=f"{self.root_key}_1",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.radio(
            label="",
            options=self.QUESTION_2_OPTIONS,
            key=f"{self.root_key}_2",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.radio(
            label="",
            options=self.QUESTION_3_OPTIONS,
            key=f"{self.root_key}_3",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_4)
        st.radio(
            label="",
            options=self.QUESTION_4_OPTIONS,
            key=f"{self.root_key}_4",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_5)
        st.radio(
            label="",
            options=self.QUESTION_5_OPTIONS,
            key=f"{self.root_key}_5",
            horizontal=False,
            label_visibility="collapsed",
        )


class Lesson4_2(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": f"Lección {tl.LESSON_4_2_TITLE}",
            "en": f"Lesson {tl.LESSON_4_2_TITLE}",
        }[self.tl.lang]
        self.root_key = "lesson_4_2"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Has conseguido estar en la red más tiempo que tus rivales?",
            "en": "Have you managed to stay in the net longer than your rivals?",
        }[self.tl.lang]

        self.QUESTION_1_OPTIONS = {
            "es": [
                "Sí, he estado más tiempo en la red que mis rivales",
                "No, no he estado más tiempo en la red que mis rivales",
                "Creo que estuvimos igual de tiempo en la red que nuestros rivales",
            ],
            "en": [
                "Yes, I was at the net more than my opponents",
                "No, I wasn't at the net more than my opponents",
                "I think we were at the net around the same amount of time as our opponents",
            ],
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Has conseguido volear por delante y en dirección a tu rival?",
            "en": "Have you managed to volley ahead and in the direction of your opponent?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": [
                "Sí, he jugado voleas por delante y en dirección al jugador",
                "No, no he jugado voleas por delante y en dirección al jugador",
                "No logré hacerlo consistentemente",
            ],
            "en": [
                "Yes, I played volleys in front of and in the direction of the players",
                "No, I didn't play volleys in front of and in the direction of the players",
                "I didn't manage to do it consistently",
            ],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Habéis logrado jugar ordenados? ¿Habéis estado sincronizados?",
            "en": "Did you manage to follow orderly play, and were you synchronized?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": [
                "Sí, hemos jugado ordenados y hemos estado sincronizados",
                "Más o menos, hemos jugado ordenados, pero no hemos estado sincronizados",
                "Más o menos, hemos estado sincronizados, pero no hemos jugado ordenados",
                "No, no hemos jugado ordenados y no hemos estado sincronizados",
            ],
            "en": [
                "Yes, we played orderly and were synchronized",
                "More or less, we followed orderly play, but we weren't synchronized",
                "More or less, we were synchronized, but we didn't follow orderly play",
                "No, we didn't follow orderly play and we weren't synchronized",
            ],
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "¿Qué te resulta más difícil?  ¿Jugar por delante del jugador, a sus pies o a su cadera no dominante?",
            "en": "What do you find more difficult: playing in front of the player, at their feet or at their non-dominant hip?",
        }[self.tl.lang]

        self.QUESTION_4_OPTIONS = {
            "es": [
                "Jugar por delante del jugador",
                "Jugar a sus pies",
                "Jugar a su cadera no dominante",
                "Todos me han resultado igual de difíciles",
            ],
            "en": [
                "Playing in front of the player",
                "Playing at their feet",
                "Playing at their non-dominant hip",
                "All were equally difficult for me",
            ],
        }[self.tl.lang]

        self.QUESTION_5 = {
            "es": "¿Has conseguido presionar, avanzar y que te quede una bola clara de definición?",
            "en": "Have you managed to pressure, advance and get a clear ball to finish?",
        }[self.tl.lang]

        self.QUESTION_5_OPTIONS = {
            "es": [
                "Sí, hemos conseguido presionar obtener bolas claras para definir, de manera consistente",
                "Sí, pero hemos sido inconsistentes, haciendo muchos errores",
                "Sí, pero hemos sido inconsistentes, perdiendo la red con facilidad",
                "No, no hemos conseguido presionar y obtener bolas claras para definir",
            ],
            "en": [
                "Yes, we managed to pressure and get clear balls to finish the point, consistently",
                "Yes, but we were inconsistent, making many mistakes while pressuring",
                "Yes, but we were inconsistent, losing the net position easily",
                "No, we didn't manage to pressure properly and get clear balls to finish the point",
            ],
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.radio(
            label="",
            options=self.QUESTION_1_OPTIONS,
            key=f"{self.root_key}_1",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.radio(
            label="",
            options=self.QUESTION_2_OPTIONS,
            key=f"{self.root_key}_2",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.radio(
            label="",
            options=self.QUESTION_3_OPTIONS,
            key=f"{self.root_key}_3",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_4)
        st.radio(
            label="",
            options=self.QUESTION_4_OPTIONS,
            key=f"{self.root_key}_4",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_5)
        st.radio(
            label="",
            options=self.QUESTION_5_OPTIONS,
            key=f"{self.root_key}_5",
            horizontal=False,
            label_visibility="collapsed",
        )


class Lesson4_3(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": f"Lección {tl.LESSON_4_3_TITLE}",
            "en": f"Lesson {tl.LESSON_4_3_TITLE}",
        }[self.tl.lang]
        self.root_key = "lesson_4_3"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Cómo ha ido tu lectura de bola cuando has estado en la volea? ¿Has reconocido si la bola venía a diferente velocidad, altura o profundidad?",
            "en": "How was your anticipation when you were at the net? Did you recognize if the ball was coming at a different speed, height or depth?",
        }[self.tl.lang]

        self.QUESTION_1_OPTIONS = {
            "es": [
                "Sí, he leído la bola que venía, he reconocido si venía a diferente velocidad, altura o profundidad",
                "Más o menos, he leído la bola que venía, pero no he reconocido si venía a diferente velocidad, altura o profundidad",
                "No, no he leído la bola que venía, no he reconocido si venía a diferente velocidad, altura o profundidad",
            ],
            "en": [
                "Yes, I read the next ball, I recognized if it was coming at a different speed, height or depth",
                "More or less, I read the next ball, but I didn't recognize if it was coming at a different speed, height or depth",
                "No, I didn't read the next ball, I didn't recognize if it was coming at a different speed, height or depth",
            ],
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "Si has leído la bola que venía, ¿has sido capaz de tomar la elección correcta?",
            "en": "If you were able to read the next ball, were you able to make the right decision?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": [
                "Sí, he sido capaz de tomar la elección correcta",
                "Más o menos, he sido capaz de tomar la elección correcta",
                "No, no he sido capaz de tomar la elección correcta",
            ],
            "en": [
                "Yes, I was able to make the right decision",
                "More or less, I was able to make the right decision",
                "No, I wasn't able to make the right decision",
            ],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿En algún momento has conseguido presionar y acercarte más a la red?",
            "en": "At any point, did you manage to pressure and get closer to the net?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": [
                "Sí, he conseguido presionar y acercarme más a la red",
                "Más o menos, he conseguido presionar y acercarme más a la red",
                "No, no he conseguido presionar y acercarme más a la red",
            ],
            "en": [
                "Yes, I managed to pressure and get closer to the net",
                "More or less, I managed to pressure and get closer to the net",
                "No, I didn't manage to pressure and get closer to the net",
            ],
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "¿Has probado el chancletazo? ¿Cómo ha ido?",
            "en": "Did you try the “chancletazo”—or the powerful, flat, forehand volley? How did it go?",
        }[self.tl.lang]

        self.QUESTION_4_OPTIONS = {
            "es": [
                "Sí, he probado el chancletazo y me ha ido bien",
                "Sí, he probado el chancletazo, pero no me ha ido bien",
                "No, no he probado el chancletazo",
            ],
            "en": [
                "Yes, I tried the chancletazo and it went well",
                "Yes, I tried the chancletazo, but it didn't go well",
                "No, I didn't try the chancletazo",
            ],
        }[self.tl.lang]

        self.QUESTION_5 = {
            "es": "¿Cómo te sale la volea firme?",
            "en": "How did your firm volley go?",
        }[self.tl.lang]

        self.QUESTION_5_OPTIONS = {
            "es": [
                "La volea firme me sale bien",
                "La volea firme me sale mal",
                "Siento que me sale bien, pero no logro hacerlo consistentemente",
            ],
            "en": [
                "My firm volley is good",
                "My firm volley is bad or unreliable",
                "I feel like I do it well, but I lack consistency",
            ],
        }[self.tl.lang]

        self.QUESTION_6 = {
            "es": "¿Y la volea cortada de arriba hacia abajo?",
            "en": "And the sliced, top-to-bottom volley?",
        }[self.tl.lang]

        self.QUESTION_6_OPTIONS = {
            "es": [
                "La volea cortada de arriba hacia abajo me sale bien",
                "La volea cortada de arriba hacia abajo me sale mal",
                "Siento que me sale bien, pero no logro hacerlo consistentemente",
            ],
            "en": [
                "My sliced, top-to-bottom volley is good",
                "My sliced, top-to-bottom volley is bad or unreliable",
                "I feel like I do it well, but I lack consistency",
            ],
        }[self.tl.lang]

        self.QUESTION_7 = {
            "es": "¿Y cuando te juegan a los pies?",
            "en": "And when they play at your feet?",
        }[self.tl.lang]

        self.QUESTION_7_OPTIONS = {
            "es": [
                "Cuando me juegan a los pies me sale bien",
                "Cuando me juegan a los pies me sale mal",
                "A veces me sale bien, a veces me sale mal",
            ],
            "en": [
                "When they play at my feet, I respond well",
                "When they play at my feet, I tend to make mistakes or give back an easy ball",
                "Sometimes I handle it well, sometimes I don't",
            ],
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.radio(
            label="",
            options=self.QUESTION_1_OPTIONS,
            key=f"{self.root_key}_1",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.radio(
            label="",
            options=self.QUESTION_2_OPTIONS,
            key=f"{self.root_key}_2",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.radio(
            label="",
            options=self.QUESTION_3_OPTIONS,
            key=f"{self.root_key}_3",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_4)
        st.radio(
            label="",
            options=self.QUESTION_4_OPTIONS,
            key=f"{self.root_key}_4",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_5)
        st.radio(
            label="",
            options=self.QUESTION_5_OPTIONS,
            key=f"{self.root_key}_5",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_6)
        st.radio(
            label="",
            options=self.QUESTION_6_OPTIONS,
            key=f"{self.root_key}_6",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_7)
        st.radio(
            label="",
            options=self.QUESTION_7_OPTIONS,
            key=f"{self.root_key}_7",
            horizontal=False,
            label_visibility="collapsed",
        )


class Lesson5_1(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": f"Lección {tl.LESSON_5_1_TITLE}",
            "en": f"Lesson {tl.LESSON_5_1_TITLE}",
        }[self.tl.lang]
        self.root_key = "lesson_5_1"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Has conseguido preparar antes de moverte hacia la bola?",
            "en": "Did you manage to prepare before moving towards the ball?",
        }[self.tl.lang]

        self.QUESTION_1_OPTIONS = {
            "es": [
                "Sí, he conseguido preparar antes de moverme hacia la bola",
                "No, no me da tiempo preparar antes de moverme hacia la bola",
                "No he conseguido hacerlo consistentemente",
            ],
            "en": [
                "Yes, I managed to prepare before moving towards the ball",
                "No, I didn't manage to prepare before moving towards the ball",
                "I didn't manage to do it consistently",
            ],
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Has conseguido hacer la misma preparación para los distintos golpes por encima de la cabeza?",
            "en": "Did you manage to make the same preparation for the different overhead shots?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": [
                "Sí, he conseguido hacer la misma preparación para los distintos golpes por encima de la cabeza",
                "No, no he conseguido hacer la misma preparación para los distintos golpes por encima de la cabeza",
                "No he conseguido hacerlo consistentemente",
            ],
            "en": [
                "Yes, I managed to make the same preparation for the different overhead shots",
                "No, I didn't manage to make the same preparation for all the different overhead shots",
                "I didn't manage to do it consistently",
            ],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "Si has preparado pronto, ¿has intentado tener visión periférica? ¿Cómo te ha ido?",
            "en": "If you prepared early, did you try using peripheral vision? How did it go?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": [
                "Sí, he intentado tener visión periférica y me ha ido bien",
                "Sí, he intentado tener visión periférica, pero no me ha ido bien",
                "No, no he intentado tener visión periférica",
            ],
            "en": [
                "Yes, I tried using peripheral vision and it went well",
                "Yes, I tried using peripheral vision, but it didn't go well",
                "No, I didn't try using peripheral vision",
            ],
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "¿Cómo han ido tus golpes por arriba? ¿Cuál has utilizado más?",
            "en": "How good were your overhead shots? Which one did you use the most?",
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.radio(
            label="",
            options=self.QUESTION_1_OPTIONS,
            key=f"{self.root_key}_1",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.radio(
            label="",
            options=self.QUESTION_2_OPTIONS,
            key=f"{self.root_key}_2",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.radio(
            label="",
            options=self.QUESTION_3_OPTIONS,
            key=f"{self.root_key}_3",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_4)
        st.text_area(
            label="",
            key=f"{self.root_key}_4",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )


class Lesson5_2(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": f"Lección {tl.LESSON_5_2_TITLE}",
            "en": f"Lesson {tl.LESSON_5_2_TITLE}",
        }[self.tl.lang]
        self.root_key = "lesson_5_2"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Has conseguido generar bolas fáciles en este partido?",
            "en": "Did you manage to generate easy balls in this match?",
        }[self.tl.lang]

        self.QUESTION_1_OPTIONS = {
            "es": [
                "Sí, he conseguido generar bolas fáciles",
                "No, no he conseguido generar bolas fáciles",
            ],
            "en": [
                "Yes, I managed to generate easy balls",
                "No, I didn't manage to generate easy balls",
            ],
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "Si ha sido así, ¿Cómo las has jugado?",
            "en": "If so, how did you play them?",
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "En caso de no haber conseguido generar bolas fáciles, ¿Cuál crees que ha sido el motivo?",
            "en": "If you weren't able to generate easy balls, what do you think was the reason?",
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.radio(
            label="",
            options=self.QUESTION_1_OPTIONS,
            key=f"{self.root_key}_1",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.text_area(
            label="",
            key=f"{self.root_key}_2",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.text_area(
            label="",
            key=f"{self.root_key}_3",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )


class Lesson5_3(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": f"Lección {tl.LESSON_5_3_TITLE}",
            "en": f"Lesson {tl.LESSON_5_3_TITLE}",
        }[self.tl.lang]
        self.root_key = "lesson_5_3"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Qué ha sucedido al volear al centro?",
            "en": "What happened when volleying to the center?",
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Has podido practicar tus golpes por encima de la cabeza?",
            "en": "Were you able to practice your overhead shots?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": [
                "Sí, pude practicarlos mucho",
                "Sí, pude practicarlos un poco",
                "No pude practicarlos casi nada",
            ],
            "en": [
                "Yes, I was able to practice them a lot",
                "Yes, I was able to practice them a little",
                "No, I wasn't able to practice them much at all",
            ],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Has decidido cambiar y volear en la trayectoria de los rivales o seguir voleando al centro? ¿Por qué?",
            "en": "Did you decide to change and volley in the opponents' trajectory or keep volleying to the center? Why?",
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.text_area(
            label="",
            key=f"{self.root_key}_1",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.radio(
            label="",
            options=self.QUESTION_2_OPTIONS,
            key=f"{self.root_key}_2",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.text_area(
            label="",
            key=f"{self.root_key}_3",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )


class Lesson6_1(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": f"Lección {tl.LESSON_6_1_TITLE}",
            "en": f"Lesson {tl.LESSON_6_1_TITLE}",
        }[self.tl.lang]
        self.root_key = "lesson_6_1"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Has conseguido jugar con primeros servicios?",
            "en": "Have you managed to play with first serves?",
        }[self.tl.lang]

        self.QUESTION_1_OPTIONS = {
            "es": [
                "Sí, he conseguido jugar con primeros servicios",
                "No, no he conseguido jugar con primeros servicios",
                "No logré hacerlo consistentemente",
            ],
            "en": [
                "Yes, I managed to play with first serves",
                "No, I didn't manage to play with first serves",
                "I didn't manage to do it consistently",
            ],
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Has coordinado la pausa en el momento adecuado?",
            "en": "Have you managed to coordinate the pause (split-step) at the right time?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": [
                "Sí, he coordinado la pausa en el momento adecuado",
                "No, no he coordinado la pausa en el momento adecuado",
                "No logré hacerlo consistentemente",
            ],
            "en": [
                "Yes, I managed to coordinate the pause at the right time",
                "No, I didn't manage to coordinate the pause at the right time",
                "I didn't manage to do it consistently",
            ],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Tu primera volea ha sido firme y hacia el restador?",
            "en": "Was your first volley firm and aimed at the receiver?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": [
                "Sí, mi primera volea ha sido firme y hacia el restador",
                "No, mi primera volea no ha sido firme y hacia el restador",
                "No logré hacerlo consistentemente",
            ],
            "en": [
                "Yes, my first volley was firm and aimed at the receiver",
                "No, my first volley wasn't firm and aimed at the receiver",
                "I didn't manage to do it consistently",
            ],
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "¿Consideras que cometes muchos errores tanto con tu primer saque como con la primera volea?",
            "en": "Do you consider that you make a lot of mistakes with both your first serve and first volley?",
        }[self.tl.lang]

        self.QUESTION_4_OPTIONS = {
            "es": [
                "Sí, considero que cometo muchos errores con mi primer saque y con mi primera volea",
                "No, no considero que cometa muchos errores con mi primer saque ni con mi primera volea",
                "Considero que cometo muchos errores con mi primer saque, pero no con mi primera volea",
                "Considero que cometo muchos errores con mi primera volea, pero no con mi primer saque",
            ],
            "en": [
                "Yes, I consider that I make a lot of mistakes with my first serve and first volley",
                "No, I don't consider that I make a lot of mistakes with my first serve or first volley",
                "I consider that I make a lot of mistakes with my first serve, but not with my first volley",
                "I consider that I make a lot of mistakes with my first volley, but not with my first serve",
            ],
        }[self.tl.lang]

        self.QUESTION_5 = {
            "es": "¿Has podido aprovechar y anticiparte a un mal resto con el saque de tu compañero?",
            "en": "Have you been able to anticipate and take advantage of a bad return to your partner's serve?",
        }[self.tl.lang]

        self.QUESTION_5_OPTIONS = {
            "es": [
                "Sí, he podido aprovechar y anticiparme a un mal resto con el saque de mi compañero",
                "No, no he podido aprovechar y anticiparme a un mal resto con el saque de mi compañero",
            ],
            "en": [
                "Yes, I was able to take advantage and anticipate a bad return with my partner's serve",
                "No, I wasn't able to take advantage and anticipate a bad return with my partner's serve",
            ],
        }[self.tl.lang]

        self.QUESTION_6 = {
            "es": "¿y tu compañero con tu saque?",
            "en": "and your partner with your serve?",
        }[self.tl.lang]

        self.QUESTION_6_OPTIONS = {
            "es": [
                "Sí, mi compañero ha podido aprovechar y anticiparse a un mal resto con mi saque",
                "No, mi compañero no ha podido aprovechar y anticiparse a un mal resto con mi saque",
            ],
            "en": [
                "Yes, my partner was able to take advantage and anticipate a bad return with my serve",
                "No, my partner wasn't able to take advantage and anticipate a bad return with my serve",
            ],
        }[self.tl.lang]

        self.QUESTION_7 = {
            "es": "¿Has variado tus saques?",
            "en": "Did you vary your serves?",
        }[self.tl.lang]

        self.QUESTION_7_OPTIONS = {
            "es": ["Sí, he variado mis saques", "No, no he variado mis saques"],
            "en": ["Yes, I varied my serves", "No, I didn't vary my serves"],
        }[self.tl.lang]

        self.QUESTION_8 = {
            "es": "¿cómo restaban tus saques los rivales?",
            "en": "How did your opponents return your serves?",
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.radio(
            label="",
            options=self.QUESTION_1_OPTIONS,
            key=f"{self.root_key}_1",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.radio(
            label="",
            options=self.QUESTION_2_OPTIONS,
            key=f"{self.root_key}_2",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.radio(
            label="",
            options=self.QUESTION_3_OPTIONS,
            key=f"{self.root_key}_3",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_4)
        st.radio(
            label="",
            options=self.QUESTION_4_OPTIONS,
            key=f"{self.root_key}_4",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_5)
        st.radio(
            label="",
            options=self.QUESTION_5_OPTIONS,
            key=f"{self.root_key}_5",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_6)
        st.radio(
            label="",
            options=self.QUESTION_6_OPTIONS,
            key=f"{self.root_key}_6",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_7)
        st.radio(
            label="",
            options=self.QUESTION_7_OPTIONS,
            key=f"{self.root_key}_7",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_8)
        st.text_area(
            label="",
            key=f"{self.root_key}_8",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )


class Lesson6_2(Form):
    def __init__(self, tl: Translation):
        super().__init__(tl)
        self.title = {
            "es": f"Lección {tl.LESSON_6_2_TITLE}",
            "en": f"Lesson {tl.LESSON_6_2_TITLE}",
        }[self.tl.lang]
        self.root_key = "lesson_6_2"
        self.set_specific_questions()

    def set_specific_questions(self):
        self.QUESTION_1 = {
            "es": "¿Has conseguido meter muchos restos dentro?",
            "en": "Did you manage to get many returns in?",
        }[self.tl.lang]

        self.QUESTION_1_OPTIONS = {
            "es": [
                "Sí, he conseguido meter muchos restos dentro",
                "No, no he conseguido meter muchos restos dentro",
                "Más o menos",
            ],
            "en": [
                "Yes, I managed to get many returns in",
                "No, I didn't manage to get many returns in",
                "More or less",
            ],
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "Con los primeros saques, ¿has restado por abajo a las zonas más incómodas de tus rivales?",
            "en": "With the first serves, did you serve low to the most uncomfortable areas of your opponents?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": [
                "Sí, he restado por abajo a las zonas más incómodas de mis rivales",
                "No, no he restado por abajo a las zonas más incómodas de mis rivales",
                "A veces, no tanto como quisiera",
            ],
            "en": [
                "Yes, I served down to the most uncomfortable areas of my opponents",
                "No, I didn't serve down to the most uncomfortable areas of my opponents",
                "Sometimes, not as much as I would have liked",
            ],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "Con segundos servicios, ¿has buscado globo o volcada para ganar la red?",
            "en": "With second serves, did you try to hit a lob or a chiquita to win the net?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": [
                "Sí, he usado globo o volcada para ganar la red consistentemente con segundos servicios",
                "No, no he buscado globo o volcada para ganar la red con segundos servicios",
                "A veces, no tanto como quisiera",
            ],
            "en": [
                "Yes, I consistently used a lob or a chiquita to win the net with second serves",
                "No, I didn't try to hit a lob or a chiquita to win the net with second serves",
                "Sometimes, not as much as I would have liked",
            ],
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "¿Te has sentido cómodo restando o has tenido que modificar tu posición para restar?",
            "en": "Have you felt comfortable returning the serve or have you had to modify your position to return the serve?",
        }[self.tl.lang]

        self.QUESTION_4_OPTIONS = {
            "es": [
                "Sí, me he sentido cómodo restando, sin necesidad de modificar mi posición",
                "No, no me he sentido cómodo restando, he tenido que modificar mi posición",
                "Me he sentido incómodo restando, incluso modificando mi posición",
            ],
            "en": [
                "Yes, I felt comfortable returning the serve, without needing to reposition",
                "No, I didn't feel comfortable returning the serve, I had to reposition",
                "I felt uncomfortable returning the serve, even after repositioning",
            ],
        }[self.tl.lang]

        self.QUESTION_5 = {
            "es": "¿Cómo has restado en los puntos importantes?",
            "en": "How did you return the serve during the important points?",
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.radio(
            label="",
            options=self.QUESTION_1_OPTIONS,
            key=f"{self.root_key}_1",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_2)
        st.radio(
            label="",
            options=self.QUESTION_2_OPTIONS,
            key=f"{self.root_key}_2",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_3)
        st.radio(
            label="",
            options=self.QUESTION_3_OPTIONS,
            key=f"{self.root_key}_3",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_4)
        st.radio(
            label="",
            options=self.QUESTION_4_OPTIONS,
            key=f"{self.root_key}_4",
            horizontal=False,
            label_visibility="collapsed",
        )
        h6(self.QUESTION_5)
        st.text_area(
            label="",
            key=f"{self.root_key}_5",
            height=0,
            max_chars=1000,
            label_visibility="collapsed",
        )

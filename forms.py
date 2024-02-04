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
        st.number_input("", min_value=0, max_value=100, value=0, step=1, key=f"{self.root_key}_1")
        h6(self.QUESTION_2)
        st.text_area("", key=f"{self.root_key}_2", height=0, max_chars=1000, label_visibility="collapsed")
        h6(self.QUESTION_3)
        st.radio("", options=self.QUESTION_3_OPTIONS, key=f"{self.root_key}_3", horizontal=True, label_visibility="collapsed")
        h6(self.QUESTION_4)
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
        h6(self.QUESTION_1)
        st.radio("", options=self.QUESTION_1_OPTIONS, key=f"{self.root_key}_1", horizontal=True, label_visibility="collapsed")
        h6(self.QUESTION_2)
        st.radio("", options=self.QUESTION_2_OPTIONS, key=f"{self.root_key}_2", horizontal=True, label_visibility="collapsed")
        h6(self.QUESTION_3)
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
        h6(self.QUESTION_1)
        st.radio("", options=self.QUESTION_1_OPTIONS, key=f"{self.root_key}_1", horizontal=True, label_visibility="collapsed")
        h6(self.QUESTION_2)
        st.radio("", options=self.QUESTION_2_OPTIONS, key=f"{self.root_key}_2", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_3)
        st.text_area("", key=f"{self.root_key}_3", height=0, max_chars=1000, label_visibility="collapsed")
        h6(self.QUESTION_4)
        st.text_area("", key=f"{self.root_key}_4", height=0, max_chars=1000, label_visibility="collapsed")

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
            "es": ["Sí, les incomodó más la velocidad alta", "Sí, les incomodó más la velocidad baja", "Creo que se manejaban bien con ambas velocidades", "No llegué a decifrar qué velocidad les incomodó más"],
            "en": ["Yes, they were more bothered by fast-paced play", "Yes, they were more bothered by slow-paced play", "I think they handled both speeds well", "I didn't manage to figure out which speed bothered them the most"],
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.text_area("", key=f"{self.root_key}_1", height=0, max_chars=1000, label_visibility="collapsed")
        h6(self.QUESTION_2)
        st.text_area("", key=f"{self.root_key}_2", height=0, max_chars=1000, label_visibility="collapsed")
        h6(self.QUESTION_3)
        st.text_area("", key=f"{self.root_key}_3", height=0, max_chars=1000, label_visibility="collapsed")
        h6(self.QUESTION_4)
        st.radio("", options=self.QUESTION_4_OPTIONS, key=f"{self.root_key}_4", horizontal=False, label_visibility="collapsed")

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
            "es": ["Sí, los distinguí", "No, no los pude distinguir", "Más o menos, tengo dudas"],
            "en": ["Yes, I identified them", "No, I didn't identify them", "I'm not so sure, I have doubts"],
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Has logrado jugar a esos espacios?",
            "en": "Were you able to play to the spaces?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": ["Sí, logré jugar a los espacios", "No, no logré jugar a los espacios", "No logré hacerlo consistentemente"],
            "en": ["Yes, I managed to play to the spaces", "No, I didn't manage to play to the spaces", "I didn't manage to do it consistently"],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Has conseguido desplazarlos hacia atrás y hacia delante?",
            "en": "Did you manage to make your opponents run back and forth?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": ["Sí, los desplacé hacia atrás y hacia delante", "No, no logré desplazarlos", "No logré hacerlo consistentemente"],
            "en": ["Yes, I made them run back and forth", "No, I didn't manage to make them run back and forth", "I didn't manage to do it consistently"],
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "Cuéntanos qué te ha resultado más fácil o más difícil del objetivo de hoy.",
            "en": "Tell us what you found the easiest or the most difficult about today's objective.",
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.radio("", options=self.QUESTION_1_OPTIONS, key=f"{self.root_key}_1", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_2)
        st.radio("", options=self.QUESTION_2_OPTIONS, key=f"{self.root_key}_2", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_3)
        st.radio("", options=self.QUESTION_3_OPTIONS, key=f"{self.root_key}_3", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_4)
        st.text_area("", key=f"{self.root_key}_4", height=0, max_chars=1000, label_visibility="collapsed")

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
            "es": ["Sí, los preparé pronto o más pronto que antes", "No, no los preparé pronto, sentí que me faltaba tiempo", "No logré hacerlo consistentemente, en ocasiones sí, en ocasiones no"],
            "en": ["Yes, I prepared them early or earlier than before", "No, I didn't prepare them early, I felt I lacked time to do it well", "I didn't manage to do it consistently, sometimes yes, sometimes not"]
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Has utilizado la misma preparación para tu golpe de derecha? ¿y de revés?",
            "en": "Have you managed to achieve a consistent, repetitive motion for your forehand? What about your backhand?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": ["Logré ser consistente en la preparación de ambos golpes", "Logré ser consistente en el golpe de derecha, pero no en el de revés", "Logré ser consistente en el golpe de revés, pero no en el de derecha", "No logré ser consistente en la preparación de ninguno de los dos golpes"],
            "en": ["I managed to be consistent in the preparation of both shots", "I managed to be consistent in the forehand, but not in the backhand", "I managed to be consistent in the backhand, but not in the forehand", "I didn't manage to be consistent in the preparation of either shot"],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Has llegado al objetivo de engañar a tus rivales?",
            "en": "Have you reached the goal of deceiving your rivals?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": ["Sí, logré engañar a mis rivales", "No, no logré engañar a mis rivales", "Logré hacerlo una o dos veces solamente"],
            "en": ["Yes, I managed to deceive my opponents", "No, I didn't manage to deceive my opponents", "I only managed to do it once or twice"],
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.radio("", options=self.QUESTION_1_OPTIONS, key=f"{self.root_key}_1", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_2)
        st.radio("", options=self.QUESTION_2_OPTIONS, key=f"{self.root_key}_2", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_3)
        st.radio("", options=self.QUESTION_3_OPTIONS, key=f"{self.root_key}_3", horizontal=False, label_visibility="collapsed")

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
            "es": ["Muy bien, logré enfocarme en el objetivo desde el inicio e hice pocos errores", "Bien, logré enfocarme en el objetivo desde el inicio, pero cometí más errores de los que me hubiera gustado", "Regular, no logré enfocarme en el objetivo desde el inicio y cometí más errores de los que me hubiera gustado", "Mal, no logré enfocarme en el objetivo desde el inicio y cometí muchos errores"],
            "en": ["Very well, I managed to focus on the goal from the start and made few mistakes", "Good, I managed to focus on the goal from the start, but made more mistakes than I would have liked", "Regular, I didn't manage to focus on the goal from the start and made more mistakes than I would have liked", "Bad, I didn't manage to focus on the goal from the start and made many mistakes"],
        }[self.tl.lang]

        self.QUESTION_2 = {
            "es": "¿Has conseguido jugar a las zonas más incómodas para tu rival?",
            "en": "Did you manage to play to the most uncomfortable areas for your opponent?",
        }[self.tl.lang]

        self.QUESTION_2_OPTIONS = {
            "es": ["Sí, logré jugar a las zonas más incómodas", "No, no logré jugar a las zonas más incómodas", "No logré hacerlo consistentemente"],
            "en": ["Yes, I managed to play to the most uncomfortable areas", "No, I didn't manage to play to the most uncomfortable areas", "I didn't manage to do it consistently"],
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
            "en": ["Yes", "No", "I didn't manage to do it consistently enough to be sure"],
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.radio("", options=self.QUESTION_1_OPTIONS, key=f"{self.root_key}_1", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_2)
        st.radio("", options=self.QUESTION_2_OPTIONS, key=f"{self.root_key}_2", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_3)
        st.text_area("", key=f"{self.root_key}_3", height=0, max_chars=1000, label_visibility="collapsed")
        h6(self.QUESTION_4)
        st.radio("", options=self.QUESTION_4_OPTIONS, key=f"{self.root_key}_4", horizontal=False, label_visibility="collapsed")

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
            "es": ["Sí, me he posicionado bien", "No, no me he posicionado bien", "No logré hacerlo consistentemente"],
            "en": ["Yes, I positioned myself well", "No, I didn't position myself well", "I didn't manage to do it consistently"],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Consigues jugar el globo y dejar de mirar la bola y observar al jugador que golpea?",
            "en": "Did you manage to make the lob and watch the striking opponent's positioning instead of the ball?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": ["Sí, lo consigo", "No, no lo consigo", "No logré hacerlo consistentemente"],
            "en": ["Yes", "No", "I didn't manage to do it consistently"],
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "¿Has conseguido bloquear hacia el jugador que golpea?",
            "en": "Have you managed to block towards the striking player?",
        }[self.tl.lang]

        self.QUESTION_4_OPTIONS = {
            "es": ["Sí, logré bloquear bien y hacia el jugador que golpea", "Sí logré bloquear, pero sin poder controlar la dirección", "No, no logré bloquear bien"],
            "en": ["Yes, I managed to block well and towards the player who was striking", "Yes, I managed to block, but without being able to control the direction", "No, I didn't manage to block properly"],
        }[self.tl.lang]

        self.QUESTION_5 = {
            "es": "¿Has sido capaz de bajar la velocidad en el bloqueo?",
            "en": "Have you been able to slow down the ball while blocking?",
        }[self.tl.lang]

        self.QUESTION_5_OPTIONS = {
            "es": ["Sí, logré bajar la velocidad", "No, no logré bajar la velocidad", "No logré hacerlo consistentemente"],
            "en": ["Yes, I managed to lower the speed", "No, I didn't manage to lower the speed", "I didn't manage to do it consistently"],
        }[self.tl.lang]

        self.QUESTION_6 = {
            "es": "¿Ha habido muchos errores? ¿Te has encontrado cómodo/a?",
            "en": "Did you make many mistakes? Did you feel comfortable?",
        }[self.tl.lang]

        self.QUESTION_6_OPTIONS = {
            "es": ["Sí, me he encontrado cómodo/a, sin hacer muchos errores", "No, no me he encontrado cómodo/a e hice muchos errores", "Más o menos cómodo/a, hice algunos errores"],
            "en": ["Yes, I was comfortable, without making many mistakes", "No, I wasn't comfortable and made many mistakes", "More or less comfortable, I made some mistakes"],
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.text_area("", key=f"{self.root_key}_1", height=0, max_chars=1000, label_visibility="collapsed")
        h6(self.QUESTION_2)
        st.radio("", options=self.QUESTION_2_OPTIONS, key=f"{self.root_key}_2", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_3)
        st.radio("", options=self.QUESTION_3_OPTIONS, key=f"{self.root_key}_3", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_4)
        st.radio("", options=self.QUESTION_4_OPTIONS, key=f"{self.root_key}_4", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_5)
        st.radio("", options=self.QUESTION_5_OPTIONS, key=f"{self.root_key}_5", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_6)
        st.radio("", options=self.QUESTION_6_OPTIONS, key=f"{self.root_key}_6", horizontal=False, label_visibility="collapsed")


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
            "es": ["Sí, las he utilizado todas", "Casi, me faltó sólo ganar la red con la volcada", "Casi, me faltó ganar la red con el globo que NO sobrepasa", "Casi, me faltó ganar la red con el globo que sobrepasa", "No, sólo logré ganar la red con una de las opciones (La volcada)", "No, sólo logré ganar la red con una de las opciones (El globo que NO sobrepasa)", "No, sólo logré ganar la red con una de las opciones (El globo que sobrepasa)"],
            "en": ["Yes, I used them all", "Almost, I only missed winning the net with the chiquita", "Almost, I only missed winning the net with the lob that does NOT pass them", "Almost, I only missed winning the net with the lob that does overtake them", "No, I only managed to win the net with one of the options (The chiquita)", "No, I only managed to win the net with one of the options (The lob that does NOT pass them)", "No, I only managed to win the net with one of the options (The lob that does overtake them)"],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Cuál te resulta más cómoda?",
            "en": "Which one did you find more comfortable?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": ["La volcada", "El globo que NO sobrepasa", "El globo que sobrepasa"],
            "en": ["The chiquita", "The lob that does NOT pass them", "The lob that does overtake them"],
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "¿Cuál te cuesta más?",
            "en": "Which one did you find more difficult?",
        }[self.tl.lang]

        self.QUESTION_4_OPTIONS = {
            "es": ["La volcada", "El globo que NO sobrepasa", "El globo que sobrepasa"],
            "en": ["The chiquita", "The lob that does NOT pass them", "The lob that does overtake them"],
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
            "en": ["Yes, I manage to stay calm", "No, I get anxious when going up to block"],
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.text_area("", key=f"{self.root_key}_1", height=0, max_chars=1000, label_visibility="collapsed")
        h6(self.QUESTION_2)
        st.radio("", options=self.QUESTION_2_OPTIONS, key=f"{self.root_key}_2", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_3)
        st.radio("", options=self.QUESTION_3_OPTIONS, key=f"{self.root_key}_3", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_4)
        st.radio("", options=self.QUESTION_4_OPTIONS, key=f"{self.root_key}_4", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_5)
        st.text_area("", key=f"{self.root_key}_5", height=0, max_chars=1000, label_visibility="collapsed")
        h6(self.QUESTION_6)
        st.radio("", options=self.QUESTION_6_OPTIONS, key=f"{self.root_key}_6", horizontal=False, label_visibility="collapsed")
        

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
            "es": ["Sí, me he sentido más cómodo/a", "Más o menos, me he sentido igual de cómodo/a", "No, me he sentido menos cómodo/a aún"],
            "en": ["Yes, I felt more comfortable", "More or less, I felt equally comfortable", "No, I felt even less comfortable"],
        }[self.tl.lang]

        self.QUESTION_3 = {
            "es": "¿Has conseguido compenetrarte con tu compañero/a?",
            "en": "Have you been able to get along with your partner?",
        }[self.tl.lang]

        self.QUESTION_3_OPTIONS = {
            "es": ["Sí, me he compenetrado con mi compañero/a", "Neutral, me he compenetrado sólo un poco con mi compañero/a", "No, no me he comunicado mucho con mi compañero/a", "Me he llevado mal con mi compañero/a!"],
            "en": ["Yes, I got along with my partner", "Neutral, I got along with my partner, but just a little", "No, I didn't communicate much with my partner", "I got along badly with my partner!"],
        }[self.tl.lang]

        self.QUESTION_4 = {
            "es": "¿Qué te ha resultado más fácil o difícil?",
            "en": "What has been easier or harder for you?",
        }[self.tl.lang]

    def render_specific_questions(self):
        h6(self.QUESTION_1)
        st.text_area("", key=f"{self.root_key}_1", height=0, max_chars=1000, label_visibility="collapsed")
        h6(self.QUESTION_2)
        st.radio("", options=self.QUESTION_2_OPTIONS, key=f"{self.root_key}_2", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_3)
        st.radio("", options=self.QUESTION_3_OPTIONS, key=f"{self.root_key}_3", horizontal=False, label_visibility="collapsed")
        h6(self.QUESTION_4)
        st.text_area("", key=f"{self.root_key}_4", height=0, max_chars=1000, label_visibility="collapsed")


class Lesson4_1(Form):
    ...

class Lesson4_2(Form):
    ...

class Lesson4_3(Form):
    ...

class Lesson5_1(Form):
    ...

class Lesson5_2(Form):
    ...

class Lesson5_3(Form):
    ...

class Lesson6_1(Form):
    ...

class Lesson6_2(Form):
    ...

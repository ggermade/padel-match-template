import streamlit as st

from utils.fmt import h1, h2, h3


class Translation:
    def __repr__(self) -> str:
        return f"Translation({self.lang})"

    def __str__(self) -> str:
        return f"Translation({self.lang})"

    def select_language(self):
        return st.radio(
            self.SETTINGS_LANGUAGE_TITLE,
            self.SETTINGS_LANGUAGE_OPTIONS,
            horizontal=True,
            key="language",
        )

    @staticmethod
    def language_format_func(language: str) -> str:
        return {
            "English": "en",
            "Spanish": "es",
            "Español": "es",
            "Inglés": "en",
            "en": "en",
            "es": "es",
        }[language]

    def __init__(self, lang: str):
        self.lang = lang
        #### PAGE CONFIG ####
        self.PAGE_TITLE = {
            "en": "Avanza Method",
            "es": "Método Avanza",
        }[self.lang]

        self.PAGE_ICON = "static/img/logo_avanza.webp"

        # HOME
        self.HOME = {"en": "Home", "es": "Inicio"}[self.lang]
        self.HOME_TITLE = {"en": "Avanza Method: Post-Match Forms", "es": "Método Avanza: Cuestionarios Post-Partido"}[self.lang]
        self.HOME_DESCRIPTION = {
            "en": """
                Welcome to the Avanza Method! This is a collection of forms (questionnaires) to help you improve your padel game through self-reflection from your matches. 
                
                Try to fill out the forms after each match, and you will see your game improve over time.

                You can find the forms in the left sidebar (You can toggle it at the top left of the screen, or using the button down below). 
                
                Each questionnaire is oriented to a specific lesson, which you can find in [the Avanza Method Academy.](https://www.metodoavanza.com/library)

                By filling out the post-match forms, you will be contributing to your own development as a player, and you will also be helping our coaches better understand your needs and personalize your training.

                Additionally, you will soon be able to see your answers in a personalized dashboard, which will help you see your progress over time.

                Thank you for your participation!

                ♥ The Avanza Method Team
            """,
            "es": """
                Bienvenidos al Método Avanza! Esta es una colección de cuestionarios para ayudarte a mejorar tu juego de pádel con la auto-reflexión sobre tus partidos. 
                
                Intenta llenar los cuestionarios después de cada partido, y verás cómo tu juego mejora con el tiempo.

                Puedes encontrar los cuestionarios en la barra lateral izquierda. Puedes abrirla o cerrarla en la esquina superior izquierda de la pantalla, o usando el botón de abajo.
                
                Cada cuestionario está orientado a una lección específica, que puedes encontrar en la [Academia de Método Avanza.](https://www.metodoavanza.com/library)

                Al llenar los cuestionarios, estarás contribuyendo a tu propio desarrollo como jugador, y también estarás ayudando a los entrenadores a entender mejor tus necesidades y a personalizar tu entrenamiento. 

                Además, pronto podrás ver tus respuestas en un tablero de control personalizado, que te ayudará a ver tu progreso a lo largo del tiempo.

                ¡Gracias por tu participación!

                ♥ El Equipo de Método Avanza
            """,
        }[self.lang]

        # PAGES
        self.MENU = {"en": "Menu", "es": "Menú"}[self.lang]
        self.LESSON_1_1_TITLE = {
            "en": "1.1: Consistency",
            "es": "1.1: La Consistencia",
        }[self.lang]
        self.LESSON_1_2_TITLE = {
            "en": "1.2: The 5 Objectives of a Match",
            "es": "1.2: Los 5 Objetivos de un Partido",
        }[self.lang]
        self.LESSON_1_3_TITLE = {
            "en": "1.3: Easy or Difficult Balls in the Defense",
            "es": "1.3: Bolas Fáciles o Difíciles en la Defensa",
        }[self.lang]

        #### LOGIN ####
        self.LOGIN_TITLE = {"en": "Login", "es": "Inicio de Sesión"}[self.lang]
        self.USERNAME = {"en": "Username", "es": "Nombre de Usuario"}[self.lang]
        self.PASSWORD = {"en": "Password", "es": "Contraseña"}[self.lang]
        self.LOGIN_BUTTON = {"en": "Log in", "es": "Iniciar Sesión"}[self.lang]
        self.LOGOUT_BUTTON = {"en": "Log out", "es": "Cerrar Sesión"}[self.lang]

        #### MAIN ####
        self.MAIN_TITLE = {
            "en": "Avanza Method Forms",
            "es": "Cuestionarios Método Avanza",
        }[self.lang]

        self.QUESTIONNAIRE_TITLE = {
            "en": "Post-Match Total Self-Evaluation",
            "es": "Auto-Evaluación Total Post-Partido",
        }[self.lang]

        self.SUBMIT_BUTTON = {"en": "Submit", "es": "Enviar"}[self.lang]
        self.SUBMIT_SUCCESS = {
            "en": "Submitted successfully",
            "es": "Enviado con éxito",
        }[self.lang]

        #### AUTH ####

        self.SETTINGS_TITLE = {"en": "Settings", "es": "Configuraciones"}[self.lang]

        self.SETTINGS_LANGUAGE_TITLE = {
            "en": "Idioma / Language",
            "es": "Idioma / Language",
        }[self.lang]

        self.SETTINGS_LANGUAGE_OPTIONS = {
            "en": ["Español", "English"],
            "es": ["Español", "English"],
        }[self.lang]

        #### QUESTIONS ####
        self.INTRODUCTORY_MD = {
            "en": """
                This post-match template is used to great effect when you win an even match, but above all else, where it is most effective is when used after the matches you lose. In these matches you're going to reflect on more things to improve.

                ## Introduction
                The best thing to do is to ask yourself questions in each of the areas where you can improve.

                These questions are a guide, something to help you unpack the match and bring out lots of ideas and tools to develop little by little.

                The idea is that progressively, as you play matches and analyze them after playing, you continue to expand your knowledge of all the skills that you can improve and that influence the outcome of a match.

                Eventually you'll internalize all these details, and you'll become better and better at reading your matches and opponents.

                The most important thing about this template is that you know:
                - Where you have failed
                -What your rivals did well
                -What changes would you have to make if you were to play the same match again?
            """,
            "es": """
                Esta plantilla post-partido es aconsejable que la utilices cuando ganes un partido igualado, pero sobre todo donde es más efectiva es en los partidos que pierdas. En estos partidos vas a ver más cosas que mejorar. 

                ## Introducción 
                Lo mejor, es hacerte preguntas en cada una de las áreas en las que puedes mejorar.

                Estas preguntas son una guía, algo que te sirva para desgranar el partido y que saques muchas ideas y recursos para ir desarrollando poco a poco. 


                De lo que se trata es que progresivamente, a medida que juegues partidos y hagas un análisis de ellos después de jugar, vayas ampliando tu conocimiento de todas las habilidades que puedes mejorar y que influyen en un partido. 

                Llegará un momento, que toda esta información esté en tu cabeza y serás capaz de leer mejor tus partidos y a tus rivales.

                Lo más importante de este cuestionario es que sepas:
                - En qué habéis fallado
                - En qué han acertado los rivales
                - Qué cambios tendrías que hacer si jugaras el mismo partido de nuevo
            """,
        }[self.lang]

        self.DATA_COLLECTION_TITLE = {
            "en": "Data Collection",
            "es": "Toma de Datos",
        }[self.lang]

        self.PRE_MATCH_TITLE = {
            "en": "Before the Match",
            "es": "Antes del Partido",
        }[self.lang]

        self.PHYSICAL_TITLE = {
            "en": "Physical Performance",
            "es": "Desempeño Físico",
        }[self.lang]

        self.MENTAL_EMOTIONAL_TITLE = {
            "en": "Mental & Emotional State",
            "es": "Estado Mental y Emocional",
        }[self.lang]

        self.TECHNICAL_TACTICAL_STRATEGIC_TITLE = {
            "en": "Technique, Tactics, & Strategy",
            "es": "Nivel Técnico-Táctico-Estratégico",
        }[self.lang]

        # Data Collection
        self.MATCH_DATE = {
            "en": "Match date",
            "es": "Fecha del partido",
        }[self.lang]

        self.OPPONENT_1 = {
            "en": "Opponent 1",
            "es": "Nombre Rival 1",
        }[self.lang]

        self.OPPONENT_2 = {
            "en": "Opponent 2",
            "es": "Nombre Rival 2",
        }[self.lang]

        self.RESULT = {
            "en": "Result",
            "es": "Resultado",
        }[self.lang]

        self.RESULT_OPTIONS = {
            "en": ["Match Result", "Win", "Draw", "Loss"],
            "es": ["Elige un Resultado", "Victoria", "Empate", "Derrota"],
        }[self.lang]

        # PRE_MATCH
        self.PRE_MATCH_1 = {
            "en": "Did you have some time for yourself, to focus on the match and really concentrate?",
            "es": "¿Has tenido algo de tiempo para tí, para enfocarte en el partido y concentrarte?",
        }[self.lang]

        self.PRE_MATCH_1_OPTIONS = {
            "en": ["Yes", "No", "Just a little bit"],
            "es": ["Sí", "No", "Solo un poco"],
        }[self.lang]

        self.PRE_MATCH_2 = {
            "en": "Where you able to physically warm up before beginning?",
            "es": "¿Has podido calentar físicamente antes de entrar?",
        }[self.lang]

        self.PRE_MATCH_2_OPTIONS = {
            "en": ["Yes", "No", "Just a little bit"],
            "es": ["Sí", "No", "Solo un poco"],
        }[self.lang]

        self.PRE_MATCH_3 = {
            "en": "Did you know the rivals from beforehand, and came in with a predetermined strategy?",
            "es": "¿Conocías a los rivales y llevabas una estrategia predeterminada?",
        }[self.lang]

        self.PRE_MATCH_3_OPTIONS = {
            "en": ["Yes", "No"],
            "es": ["Sí", "No"],
        }[self.lang]

        self.PRE_MATCH_3_TEXT = {
            "en": "If so, what was the strategy?",
            "es": "Si es así, ¿cuál era la estrategia?",
        }[self.lang]

        self.PRE_MATCH_4 = {
            "en": "Have you talked to your partner before the match and discussed how you plan to play?",
            "es": "¿Has hablado con tu pareja antes del partido y os habéis planteado cómo jugar?",
        }[self.lang]

        self.PRE_MATCH_4_OPTIONS = {
            "en": ["Yes", "No"],
            "es": ["Sí", "No"],
        }[self.lang]

        self.PRE_MATCH_5 = {
            "en": "How did it go in the warm-up? What feelings did you get from your physique and from the quality of your strokes?",
            "es": "¿Cómo te ha ido en el peloteo? ¿Qué sensaciones físicas y en tus golpes has tenido? ",
        }[self.lang]

        self.PRE_MATCH_6 = {
            "en": "Before the start of the match, did you talk to your partner about how your opponents played in the warm-up rallies?",
            "es": "Antes de comenzar el partido, ¿has hablado con tu pareja sobre cómo estaban en el peloteo vuestros rivales?",
        }[self.lang]

        self.PRE_MATCH_6_OPTIONS = {
            "en": ["Yes", "No"],
            "es": ["Sí", "No"],
        }[self.lang]

        # Physical
        self.PHYSICAL_1 = {
            "en": "How did you feel during the match?",
            "es": "¿Cómo has estado físicamente durante el partido?",
        }[self.lang]

        self.PHYSICAL_2 = {
            "en": "Did you feel tired during the match?",
            "es": "¿Estabas cansado durante el partido?",
        }[self.lang]

        self.PHYSICAL_2_OPTIONS = {
            "en": ["Yes", "No", "Kind of"],
            "es": ["Sí", "No", "Más o menos"],
        }[self.lang]

        self.PHYSICAL_3 = {
            "en": "Were you moving fast and with a good feeling? ",
            "es": "¿Te has sentido rápido y con buenas sensaciones?",
        }[self.lang]

        self.PHYSICAL_3_OPTIONS = {
            "en": ["Yes", "No", "Kind of"],
            "es": ["Sí", "No", "Más o menos"],
        }[self.lang]

        self.PHYSICAL_4 = {
            "en": "Have you noticed that you lacked stamina or reaction speed at any time during the match?",
            "es": "¿Has notado que te ha faltado resistencia o velocidad de reacción en algún momento del partido?",
        }[self.lang]

        self.PHYSICAL_4_OPTIONS = {
            "en": ["Yes", "No"],
            "es": ["Sí", "No"],
        }[self.lang]

        self.PHYSICAL_5 = {
            "en": "If you weren't as you would have liked to be, what did you try to make a change?",
            "es": "Si no has estado como te gustaría, ¿qué has intentado para cambiarlo?",
        }[self.lang]

        # Mental Emotional
        self.MENTAL_1 = {
            "en": "Have you maintained your attention and concentration throughout the match?",
            "es": "¿Has mantenido durante todo el partido tu atención y concentración?",
        }[self.lang]

        self.MENTAL_1_OPTIONS = {
            "en": ["Yes", "No"],
            "es": ["Sí", "No"],
        }[self.lang]

        self.MENTAL_2 = {
            "en": "If at any time you lost it, did you become aware early on and know how to reconnect into the match?",
            "es": "Si en algún momento la has perdido, ¿has sido consciente pronto y has sabido reconducirte?",
        }[self.lang]

        self.MENTAL_2_OPTIONS = {
            "en": ["Yes", "No"],
            "es": ["Sí", "No"],
        }[self.lang]

        self.MENTAL_3 = {
            "en": "How was your attitude?",
            "es": "¿Cómo ha sido tu actitud?",
        }[self.lang]

        self.MENTAL_3_OPTIONS = {
            "en": ["Positive", "Negative", "Neutral"],
            "es": ["Positiva", "Negativa", "Neutral"],
        }[self.lang]

        self.MENTAL_4 = {
            "en": "What thoughts did you have?",
            "es": "¿Cuáles han sido tus pensamientos?",
        }[self.lang]

        self.MENTAL_5 = {
            "en": "Did you feel yourself driven by frustration or anxiety?",
            "es": "¿Te has dejado llevar por la frustración o la ansiedad?",
        }[self.lang]

        self.MENTAL_5_OPTIONS = {
            "en": ["Yes", "No"],
            "es": ["Sí", "No"],
        }[self.lang]

        self.MENTAL_6 = {
            "en": "If so, what did you try to overcome that mindset?",
            "es": "Si ha sido así, ¿qué has hecho para salir de ahí?",
        }[self.lang]

        self.MENTAL_7 = {
            "en": "You know how it feels when you're playing well and move with ease through the court. On the days when you don't have those good sensations, what do you do to try to get them?",
            "es": "Sabes las  sensaciones que tienes cuando juegas bien y estás a gusto en la pista. En los días en los que no tienes esas sensaciones, ¿qué haces para conseguirlas?",
        }[self.lang]

        self.MENTAL_8 = {
            "en": "What did you think about during the breaks for changing sides? ",
            "es": "¿Qué has pensado en los cambios de lado? ",
        }[self.lang]

        self.MENTAL_9 = {
            "en": "What feelings did you have when leaving the game?",
            "es": "¿Con qué sensación has salido del partido?",
        }[self.lang]

        # Technical

        self.TECHNICAL_1 = {
            "en": "What level did your rivals have? Were they superior? Were they similar? Or were they inferior?",
            "es": "¿Qué nivel tenían tus rivales? ¿eran superiores a vosotros? ¿similares? ¿inferiores?",
        }[self.lang]

        self.TECHNICAL_1_OPTIONS = {
            "en": ["Superior", "Similar", "Inferior"],
            "es": ["Superior", "Similar", "Inferior"],
        }[self.lang]

        self.TECHNICAL_2 = {
            "en": "Was one of your rivals better or did more damage than their teammate?",
            "es": "¿Alguno de vuestros rivales era mejor o hacía más daño?",
        }[self.lang]

        self.TECHNICAL_2_OPTIONS = {
            "en": ["Yes", "No"],
            "es": ["Sí", "No"],
        }[self.lang]

        self.TECHNICAL_3 = {
            "en": "How was your level of play in the defense?",
            "es": "¿Cómo habéis estado en la defensa?",
        }[self.lang]

        self.TECHNICAL_3_OPTIONS = {
            "en": ["Good", "Bad", "Regular"],
            "es": ["Bien", "Mal", "Regular"],
        }[self.lang]

        self.TECHNICAL_4 = {
            "en": "Were you able to provoke easy balls to try to win the net?",
            "es": "¿Habéis provocado bolas para intentar ganar la red?",
        }[self.lang]

        self.TECHNICAL_4_OPTIONS = {
            "en": ["Yes", "No", "Not as much as we would have liked"],
            "es": ["Sí", "No", "No tanto como nos hubiera gustado"],
        }[self.lang]

        self.TECHNICAL_5 = {
            "en": "Did you manage to play to their most uncomfortable areas?",
            "es": "¿Habéis jugado a sus zonas más incómodas?",
        }[self.lang]

        self.TECHNICAL_5_OPTIONS = {
            "en": ["Yes", "No", "Not as much as we would have liked"],
            "es": ["Sí", "No", "No tanto como nos hubiera gustado"],
        }[self.lang]

        self.TECHNICAL_6 = {
            "en": "Were you able to spend more time at the net than your rivals?",
            "es": "¿Habéis estado más tiempo en la red que vuestros rivales?",
        }[self.lang]

        self.TECHNICAL_6_OPTIONS = {
            "en": ["Yes", "No", "About the same"],
            "es": ["Sí", "No", "Más o menos igual que ellos"],
        }[self.lang]

        self.TECHNICAL_7 = {
            "en": "Did you lose the net easily?",
            "es": "¿Perdíais la red con facilidad?",
        }[self.lang]

        self.TECHNICAL_7_OPTIONS = {
            "en": ["Yes", "No", "Somewhat"],
            "es": ["Sí", "No", "Neutral, más o menos"],
        }[self.lang]

        self.TECHNICAL_8 = {
            "en": "Did you get clear balls to hit winners after working/constructing the point?",
            "es": "¿Llegaban bolas para definir después de trabajar el punto?",
        }[self.lang]

        self.TECHNICAL_8_OPTIONS = {
            "en": ["Yes", "No", "Not as much as we would have liked"],
            "es": ["Sí", "No", "No tanto como nos hubiera gustado"],
        }[self.lang]

        self.TECHNICAL_9 = {
            "en": "How have your serving games been going? How many serving games did you lose?",
            "es": "¿Cómo han ido vuestros juegos con saque? ¿Cuántos juegos con saque habéis perdido?",
        }[self.lang]

        self.TECHNICAL_10 = {
            "en": "What about your returning games? Did you ever manage to break your opponents' serve?",
            "es": "¿Y vuestros juegos al resto? ¿habéis conseguido romper el servicio de vuestros rivales alguna vez?",
        }[self.lang]

        self.TECHNICAL_10_OPTIONS = {
            "en": ["Yes", "No"],
            "es": ["Sí", "No"],
        }[self.lang]

        self.TECHNICAL_11 = {
            "en": "When something didn't work out, did you talk to your partner to try out other things?",
            "es": "Cuando algo no salía, ¿hablabas con tu compañero para tratar de hacer otras cosas?",
        }[self.lang]

        self.TECHNICAL_11_OPTIONS = {
            "en": ["Yes", "No"],
            "es": ["Sí", "No"],
        }[self.lang]

        self.TECHNICAL_12 = {
            "en": "Do you think you followed the right strategy?",
            "es": "¿Crees que habéis seguido la estrategia adecuada?",
        }[self.lang]

        self.TECHNICAL_12_OPTIONS = {
            "en": ["Yes", "No"],
            "es": ["Sí", "No"],
        }[self.lang]

        self.TECHNICAL_13 = {
            "en": "If not, what changes do you think you should have made? That is, if you were to play this match again, what changes would you make?",
            "es": "Si no ha sido así, ¿qué cambios crees que tendríais que haber hecho?. Es decir, si volvieras a jugar este partido, ¿qué cambios harías?",
        }[self.lang]

        self.TECHNICAL_14 = {
            "en": "What strategy did your rivals follow?",
            "es": "¿Qué estrategia han seguido tus rivales?",
        }[self.lang]

        self.TECHNICAL_15 = {
            "en": "Why do you think they won?",
            "es": "¿Por qué crees que han ganado?",
        }[self.lang]

class Form:
    def __repr__(self) -> str:
        return f"Form({self.tl.lang})"

    def __str__(self) -> str:
        return f"Form({self.tl.lang})"

    def __init__(self, tl: Translation) -> None:
        self.tl = tl

        # This should be implemented in the child class
        self.title: str = ""

        self.subtitle = {
            "en": "Post-Match Evaluation",
            "es": "Evaluación Post-Partido",
        }[self.tl.lang]

        self.common_questions_subheader = {
            "en": "Tell us how you felt today.",
            "es": "Cuéntanos cómo has estado hoy.",
        }[self.tl.lang]

        self.specific_questions_subheader = {
            "en": "Questions about the lesson's objectives",
            "es": "Preguntas sobre los objetivos de la lección",
        }[self.tl.lang]

        self.set_common_questions()

    def set_common_questions(self):
        self.COMMON_1 = {
            "en": "How did you feel when striking? How was your touch, wrist action, etc…?",
            "es": "¿Qué sensaciones has sentido al golpear? ¿Cómo sentiste tu toque, mano, etc…?",
        }[self.tl.lang]

        self.COMMON_2 = {
            "en": "How was your attention and concentration during the match?",
            "es": "¿Cómo has estado de atención y concentración durante el partido?",
        }[self.tl.lang]

        self.COMMON_3 = {
            "en": "How did you feel physically?",
            "es": "¿Cómo te has sentido físicamente?",
        }[self.tl.lang]

        self.COMMON_4 = {
            "en": "How was your attitude and mindset during the match?",
            "es": "¿Cómo ha sido tu actitud y mentalidad durante el partido?",
        }[self.tl.lang]

    def render_specific_questions(self):
        raise NotImplementedError("You must implement this method in the child class")

    def render_common_questions(self):
        st.write(self.COMMON_1)
        st.text_area("", key="common_1", height=0, max_chars=1000, value="", label_visibility="collapsed")
        st.write(self.COMMON_2)
        st.radio("", ["Yes", "No"], key="common_2", horizontal=True, label_visibility="collapsed")
        st.write(self.COMMON_3)
        st.radio("", ["Yes", "No"], key="common_3", horizontal=True, label_visibility="collapsed")
        st.write(self.COMMON_4)
        st.radio("", ["Yes", "No"], key="common_4", horizontal=True, label_visibility="collapsed")

    def render(self):
        h1(self.title) # From the child class
        h2(self.subtitle)
        with st.form(key="post_match_form"):
            h3(self.specific_questions_subheader)
            self.render_specific_questions()
            h3(self.common_questions_subheader)
            self.render_common_questions()
            st.form_submit_button(self.tl.SUBMIT_BUTTON)
        


    



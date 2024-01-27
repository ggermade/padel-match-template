import streamlit as st


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
            "en": "Post-Match Form",
            "es": "Cuestionario Post-Partido",
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

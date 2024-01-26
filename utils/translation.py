import streamlit as st


class Translation:
    def __repr__(self) -> str:
        return f"Translation({self.lang})"
    
    def __str__(self) -> str:
        return f"Translation({self.lang})"
    
    def select_language(self):
        return st.radio(self.SETTINGS_LANGUAGE_TITLE, self.SETTINGS_LANGUAGE_OPTIONS, horizontal=True, key="language")
    
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

        self.QUESTIONNAIRE_TITLE = {"en": "Post-Match Form", "es": "Cuestionario Post-Partido"}[
            self.lang
        ]

        self.SUBMIT_BUTTON = {"en": "Submit", "es": "Enviar"}[self.lang]
        self.SUBMIT_SUCCESS = {
            "en": "Submitted successfully",
            "es": "Enviado con éxito",
        }[self.lang]

        #### AUTH ####

        self.SETTINGS_TITLE = {"en": "Settings", "es": "Configuraciones"}[self.lang]

        self.SETTINGS_LANGUAGE_TITLE = {"en": "Idioma / Language", "es": "Idioma / Language"}[self.lang]

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

        class _QuestionText:
            # Data Collection
            MATCH_DATE = {
                "en": "Match date",
                "es": "Fecha del partido",
            }[self.lang]

            OPPONENT_1 = {
                "en": "Opponent 1",
                "es": "Nombre Rival 1",
            }[self.lang]

            OPPONENT_2 = {
                "en": "Opponent 2",
                "es": "Nombre Rival 2",
            }[self.lang]

            RESULT = {
                "en": "Result",
                "es": "Resultado",
            }[self.lang]

            RESULT_OPTIONS = {
                "en": ["Match Result", "Win", "Draw", "Loss"],
                "es": ["Elige un Resultado", "Victoria", "Empate", "Derrota"],
            }[self.lang]

            # Physical

        self.QuestionText = _QuestionText()

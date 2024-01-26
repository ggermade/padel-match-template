from utils.config import get_language

lang: str = get_language()

#### LOGIN ####
LOGIN_TITLE = {"en": "Login", "es": "Inicio de Sesión"}[lang]
USERNAME = {"en": "Username", "es": "Nombre de Usuario"}[lang]
PASSWORD = {"en": "Password", "es": "Contraseña"}[lang]
LOGIN_BUTTON = {"en": "Log in", "es": "Iniciar Sesión"}[lang]
LOGOUT_BUTTON = {"en": "Log out", "es": "Cerrar Sesión"}[lang]

#### MAIN ####
MAIN_TITLE = {
    "en": "Padel Post-Match Questionnaire",
    "es": "Cuestionario Post-Partido de Padel",
}[lang]

QUESTIONNAIRE_TITLE = {"en": "Questionnaire", "es": "Cuestionario"}[lang]

SUBMIT_BUTTON = {"en": "Submit", "es": "Enviar"}[lang]

#### AUTH ####

SETTINGS_TITLE = {"en": "Settings", "es": "Configuraciones"}[lang]

SETTINGS_LANGUAGE = {"en": "Select Language", "es": "Elige Idioma"}[lang]

SETTINGS_LANGUAGE_OPTIONS = {
    "en": ["English", "Spanish"],
    "es": ["Inglés", "Español"],
}[lang]

#### QUESTIONS ####
INTRODUCTORY_MD = {
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
}[lang]

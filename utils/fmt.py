import streamlit as st


def hr() -> None:
    """Displays a horizontal line."""
    st.markdown("***")


def h1(text: str, align: str = "center") -> None:
    """Displays a h1 title.

    Args:
        text (str): Title text.
    """
    # center the title
    st.markdown(f"<h1 style='text-align: {align};'>{text}</h1>", unsafe_allow_html=True)


def h2(text: str, align: str = "center") -> None:
    """Displays a h2 title.

    Args:
        text (str): Title text.
    """
    # center the title
    st.markdown(f"<h2 style='text-align: {align};'>{text}</h2>", unsafe_allow_html=True)


def h3(text: str, align: str = "center") -> None:
    """Displays a h3 title.

    Args:
        text (str): Title text.
    """
    # center the title
    st.markdown(f"<h3 style='text-align: {align};'>{text}</h3>", unsafe_allow_html=True)


def h4(text: str) -> None:
    """Displays a h4 title.

    Args:
        text (str): Title text.
    """
    st.markdown(f"<h4>{text}</h4>", unsafe_allow_html=True)


def h5(text: str) -> None:
    """Displays a h5 title.

    Args:
        text (str): Title text.
    """
    st.markdown(f"<h5>{text}</h5>", unsafe_allow_html=True)

def h6(text: str) -> None:
    """Displays a h6 title.

    Args:
        text (str): Title text.
    """
    st.markdown(f"<h6>{text}</h6>", unsafe_allow_html=True)


def span(text: str) -> None:
    """Displays a span.

    Args:
        text (str): Text.
    """
    st.markdown(f"<span>{text}</span>", unsafe_allow_html=True)


def br(n: int = 1) -> None:
    """Displays n line breaks."""
    for _ in range(n):
        st.markdown("<br>", unsafe_allow_html=True)

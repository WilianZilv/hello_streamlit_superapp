import streamlit as st

from streamlit_superapp.state import State


NAME = "Persistent Text Input"
DESCRIPTION = """The TextInput will recover its previous state when switching pages.
The state can be accessed and updated from any page."""
ORDER = "A"


def main():
    st.text(DESCRIPTION)

    state = State("text", default_value="Wilian")

    text = st.text_input("Your Name", value=state.initial_value, key=state.key)

    previous_text = state.bind(text)

    if text != previous_text:
        st.success(f"Input changed: {previous_text} -> {text}")

    st.success(f"Hello {text}!")

    with st.expander("Show code"):
        st.code(
            """
import streamlit as st

from streamlit_superapp.state import State


NAME = "Persistent Text Input"
DESCRIPTION = \"""The TextInput will recover its previous state when switching pages.
The state can be accessed and updated from any page.\"""
ORDER = "A"


def main():
    st.text(DESCRIPTION)

    state = State("text", default_value="Wilian")

    text = st.text_input("Your Name", value=state.initial_value, key=state.key)

    previous_text = state.bind(text)

    if text != previous_text:
        st.success(f"Input changed: {previous_text} -> {text}")

    st.success(f"Hello {text}!")

        """
        )

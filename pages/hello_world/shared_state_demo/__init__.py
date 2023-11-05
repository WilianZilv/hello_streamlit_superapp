from streamlit_superapp import State
import streamlit as st

NAME = "Shared State"
DESCRIPTION = """This example shows a TextInput that shares
the same state as the 'Persistent Text Input' page."""
ICON = "🔁"

ORDER = "B"


def main():
    st.text(DESCRIPTION)

    state = State("text", default_value="Wilian")

    value = st.text_input("Shared Text Input", value=state.initial_value, key=state.key)

    state.bind(value)

    st.write(value)

    with st.expander("Show code"):
        st.code(
            """
from streamlit_superapp import State
import streamlit as st

NAME = "Shared State"
DESCRIPTION = \"""This example shows a TextInput that shares
the same state as the 'Persistent Text Input' page.\"""
ICON = "🔁"

ORDER = "B"


def main():
    st.text(DESCRIPTION)

    state = State("text", default_value="Wilian")

    value = st.text_input("Shared Text Input", value=state.initial_value, key=state.key)

    state.bind(value)

    st.write(value)

        """
        )

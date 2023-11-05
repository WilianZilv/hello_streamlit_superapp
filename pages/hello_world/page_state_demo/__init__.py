from streamlit_superapp import State
import streamlit as st

NAME = "Page Only State"
DESCRIPTION = """This example shows a Persistent TextInput that its
value is only available in this page."""
ORDER = "Z"


def main(page):
    st.text(DESCRIPTION)

    state = State("text", default_value="", key=page)

    value = st.text_input(
        "This is not shared between pages", value=state.initial_value, key=state.key
    )

    previous_value = state.bind(value)

    st.write(value)

    if value != previous_value:
        st.success("Input changed")

    with st.expander("Show code"):
        st.code(
            """
from streamlit_superapp import State
import streamlit as st

NAME = "Page Only State"
DESCRIPTION = \"""This example shows a Persistent TextInput that its
value is only available in this page.\"""
ORDER = "Z"


def main(page):
    st.text(DESCRIPTION)

    state = State("text", default_value="", key=page)

    value = st.text_input(
        "This is not shared between pages", value=state.initial_value, key=state.key
    )

    previous_value = state.bind(value)

    st.write(value)

    if value != previous_value:
        st.success("Input changed")

        """
        )

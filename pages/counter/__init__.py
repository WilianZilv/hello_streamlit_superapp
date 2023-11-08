import streamlit as st
from common.tags import Tag
from streamlit_superapp import State


NAME = "Counter"
ICON = "🔢"


def main(page):
    counter = State("counter", default_value=0, key=page)

    if st.button("Increment"):
        counter.value += 1

    st.write(f"counter: {counter.value}")

    st.code(
        """
import streamlit as st
from common.tags import Tag
from streamlit_superapp import State


NAME = "Counter"
TAG = Tag.DEMO
ICON = "🔢"


def main(page):
    counter = State("counter", default_value=0, key=page)

    if st.button("Increment"):
        counter.value += 1

    st.write(f"counter: {counter.value}")
    """
    )

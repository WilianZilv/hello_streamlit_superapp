import pandas as pd
import streamlit as st
from common.tags import Tag

from streamlit_superapp.state import State

ICON = "📊"


def main(page):
    st.text("Put some numbers in the table and click on the button to multiply them")

    state = State("df", default_value=get_base_input(), key=page)

    with st.sidebar:
        if st.button("✖️ Multiply"):
            state.initial_value = calculate(state.value)

        if st.button("🔄 Reset"):
            state.initial_value = get_base_input()

    df = st.data_editor(data=state.initial_value, key=state.key, hide_index=True)

    previous_df = state.bind(df)

    if not df.equals(previous_df):
        st.success("Data changed!")

    st.code(
        """
import numpy as np
import pandas as pd
import streamlit as st

from streamlit_superapp.state import State

ICON = "📊"


def main(page):
    state = State("df", default_value=get_base_input(), key=page)

    with st.sidebar:
        if st.button("✖️ Multiply"):
            state.initial_value = calculate(state.value)

        if st.button("🔄 Reset"):
            state.initial_value = get_base_input()

    df = st.data_editor(data=state.initial_value, key=state.key, hide_index=True)

    previous_df = state.bind(df)

    if not df.equals(previous_df):
        st.success("Data changed!")


def get_base_input():
    return pd.DataFrame(index=[0, 1, 2], columns=["a", "b"], dtype=float)


def calculate(df: pd.DataFrame):
    df["result"] = df["a"] * df["b"]

    return df
"""
    )


def get_base_input():
    return pd.DataFrame(index=[0, 1, 2], columns=["a", "b"], dtype=float)


def calculate(df: pd.DataFrame):
    df["result"] = df["a"] * df["b"]

    return df

import streamlit as st
from streamlit_superapp import State
import pandas as pd

NAME = "Persistent Data Editor"
DESCRIPTION = """The DataEditor will recover its previous state when switching pages.
The state can be accessed and updated from any page."""
ORDER = "B"


def main():
    st.text(DESCRIPTION)

    df_state = State("df", default_value=pd.DataFrame(columns=["name", "age"]))

    df = st.data_editor(
        data=df_state.initial_value, key=df_state.key, num_rows="dynamic"
    )

    previous_df = df_state.bind(df)

    if not previous_df.equals(df):
        st.success("DataFrame changed!")

    with st.expander("Show code"):
        st.code(
            """
import streamlit as st
from streamlit_superapp import State
import pandas as pd

NAME = "Persistent Data Editor"
DESCRIPTION = \"""The DataEditor will recover its previous state when switching pages.
The state can be accessed and updated from any page.\"""
ORDER = "B"


def main():
    st.text(DESCRIPTION)

    df_state = State("df", default_value=pd.DataFrame(columns=["name", "age"]))

    df = st.data_editor(
        data=df_state.initial_value, key=df_state.key, num_rows="dynamic"
    )

    previous_df = df_state.bind(df)

    if not previous_df.equals(df):
        st.success("DataFrame changed!")

        """
        )

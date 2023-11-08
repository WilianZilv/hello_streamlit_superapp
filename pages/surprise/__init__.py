import streamlit as st

ICON = "🎉"


def main():
    st.write("Welcome to the Surprise page!")

    if st.button("Surprise"):
        st.write("You clicked the button!")
        st.balloons()

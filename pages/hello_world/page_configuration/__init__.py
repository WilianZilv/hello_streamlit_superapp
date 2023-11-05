import streamlit as st

NAME = "Page Configuration Example"
ICON = "🌟"
DESCRIPTION = "Description Example"
TAG = "{ZZZZZZZZZZZZZZZ:} Tag Example"


def main():
    st.write(
        """
    This page is a demonstration of how you can personalize each page in your Streamlit superapp.

    You can customize the following properties for each page:

    - `NAME`: This is the name of the page. By default, it's set to the file name.
    - `ICON`: This is the icon of the page. By default, it's set to 📄.
    - `DESCRIPTION`: This is a brief description of the page. By default, it's empty.
    - `TAG`: This is a tag for the page. By default, it's empty.

    All of these properties are optional. You can choose to set them as per your requirements to make your app more interactive and user-friendly.
    """
    )

    st.code(
        """
        import streamlit as st

        NAME = "Page Configuration Example"
        ICON = "🚀🎯📚🌐📈🧩🎧🎮🍕🌟"
        DESCRIPTION = "Description Example"
        TAG = "{ZZZZZZZZZZZZZZZ:} Tag Example"

        def main():
            # Your code goes here
            ...
    """
    )

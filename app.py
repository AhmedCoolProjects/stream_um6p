import streamlit as st
import streamlit_book as stb
from pathlib import Path
from glob import glob


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://www.um6p.ma/sites/default/files/logos/cropped-UM6P-CS-01-2048x583.png);
                background-repeat: no-repeat;
                width: 400px;
                object-fit: contain;
            }
            [data-testid="stSidebarNav"]::before {
                content: "My Company Name";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main():
    # Streamlit webpage properties
    st.set_page_config(layout="wide", page_icon="📚",
                       page_title="stb multipaging demo")

    add_logo()

    st.title("Streamlit Book - Multipaging Demo")

    # The native multipaging demo
    # Comments
    mkd = """
    This is a streamlit app that shows different multipaging options. 
    The native multipaging provided by streamlit is [well documented](https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app).
    TLDR; just put your pages in `pages/` folder."""
    st.markdown(mkd)
    mkd = """
    * On `single page` a single page is displayed.
    * On `chapter`, a multi-page with arrows for navigation is displayed.
    * On `book`, a book with sidebar menu with full navigation options. 
    """
    st.markdown(mkd)

    # Feedback
    stb.floating_button("https://sebastiandres.xyz")


if __name__ == "__main__":
    main()

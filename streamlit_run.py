
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg
import os


# st.set_page_config(initial_sidebar_state="collapsed")
# Set the page config at the start of the main script
st.set_page_config(
    page_title="Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

pages = ['Dashboard']

# pages = ["Indicators", "Stock Index", "Knowledge", "Resources", "GitHub"]

parent_dir = os.path.dirname(os.path.abspath(__file__))

# logo_path = os.path.join(parent_dir, "cubes.svg")

urls = {"GitHub": "https://github.com/double-tea-l/survey-tool/"}

styles = {
    "nav": {
        "background-color": "grey",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "color": "grey",
        "font-weight": "normal",
        "padding": "14px",
    }
}

options = {
    "show_menu": True,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    # logo_path=logo_path,
    urls=urls,
    styles=styles,
    options=options,
)

functions = {
    "Dash": pg.show_dash,
    # "Stock Index": pg.show_stocks,
    # "Knowledge": pg.show_knowledge
}
go_to = functions.get(page)
if go_to:
    go_to()
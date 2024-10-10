import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg
import os

# Set the page config at the start of the main script
st.set_page_config(
    page_title="Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# List of available pages in your application
pages = ["Dashboard"]  # Include other pages if they exist

# Determine the parent directory for file paths
parent_dir = os.path.dirname(os.path.abspath(__file__))

# Define URL mapping for navigation
urls = {
    'Dashboard': 'dashboard',  # Maps to your Dashboard page
    # 'GitHub': 'https://github.com/double-tea-l/survey-tool/',  # If this is a link
}

# Optional: Define styles for the navigation bar
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
        "font-weight": "normal",
        "padding": "14px",
    }
}

# Options for the navigation bar
options = {
    "show_menu": True,
    "show_sidebar": False,
}

# Create the navigation bar
page = st_navbar(
    pages,
    urls=urls,
    styles=styles,
    options=options,
)

# Define the mapping of page names to functions
functions = {
    "Dashboard": pg.show_dash,  # Ensure this function is defined in your pages module
    # Add more mappings as needed
}

# Navigate to the selected page function
go_to = functions.get(page)
if go_to:
    go_to()  # Call the function for the selected page

import os
import streamlit as st

from components.sidebar_component import sidebar_component
from router import router_mappings

st.set_page_config(
    page_title="st-sidebar-template",
    page_icon=":gorilla:",
    initial_sidebar_state="auto",
)

# setting for global.css
style_path = os.path.join(os.path.dirname(__file__), "global.css")
st.markdown("<style>" + open(style_path).read() +
            "</style>", unsafe_allow_html=True)

# SiderBar
router = sidebar_component()

# routing
if router in router_mappings:
    router_mappings[router]()

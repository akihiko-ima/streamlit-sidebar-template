import streamlit as st


def third_page() -> None:
    """Renders in a Streamlit application."""
    st.header("this is third page", divider="blue")
    st.image(image="https://picsum.photos/300/200",
             caption="this is dummy image", use_container_width=True)

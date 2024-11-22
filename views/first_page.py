import streamlit as st

from services.get_data import get_data


def first_page() -> None:
    """Renders in a Streamlit application."""
    st.header("this is first page", divider="blue")
    st.caption("Fetch dummy data")

    if st.button("Get Data", type="primary"):
        result = get_data()

        st.write("The retrieved data is as follows:")
        st.write(result)

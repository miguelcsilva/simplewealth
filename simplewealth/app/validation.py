import streamlit as st


def is_text_input_empty(text: str, message: str) -> bool:
    if not text:
        st.error(message)
        return True
    return False

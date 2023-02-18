import streamlit as st


def config_main_page() -> None:
    st.set_page_config(page_title="SimpleWealth")
    st.title("SimpleWealth")


def main() -> None:
    config_main_page()


main()

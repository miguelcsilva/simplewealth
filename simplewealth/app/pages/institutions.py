import streamlit as st

from simplewealth.database import ENGINE, METADATA
from simplewealth.database.operations import get_insert_institution_statement, insert

TABLE_INSTITUTIONS = METADATA.tables["institutions"]


def config_institutions_page() -> None:
    st.set_page_config(
        page_title="SimpleWealth - Institutions",
    )
    st.title("Institutions")


def add_institution() -> None:
    institution = st.text_input(
        label="Insert a new institution:",
    )
    if st.button("Submit"):
        submit_new_institution(institution=institution)

def submit_new_institution(institution: str) -> None:
    statement = get_insert_institution_statement(
        table=TABLE_INSTITUTIONS, institution_name=institution
    )
    insert(engine=ENGINE, statements=(statement,))

def institutions() -> None:
    config_institutions_page()
    add_institution()


institutions()

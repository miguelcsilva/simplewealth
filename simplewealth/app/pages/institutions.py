import sqlalchemy as sa
import streamlit as st

from simplewealth.database import get_engine, get_metadata
from simplewealth.database.operations import get_insert_institution_statement, insert


def config_institutions_page() -> None:
    st.set_page_config(
        page_title="SimpleWealth - Institutions",
    )
    st.title("Institutions")


def add_institution(table: sa.Table, engine: sa.Engine) -> None:
    institution_name = st.text_input(
        label="Insert a new institution:",
    )
    if st.button("Submit"):
        submit_new_institution(name=institution_name, table=table, engine=engine)


def submit_new_institution(name: str, table: sa.Table, engine: sa.Engine) -> None:
    statement = get_insert_institution_statement(table=table, name=name)
    insert(engine=engine, statements=(statement,))


def institutions() -> None:
    from simplewealth.settings import SETTINGS

    engine = get_engine(url=SETTINGS.DATABASE_URI)
    metadata = get_metadata(engine=engine)
    table_institutions = metadata.tables["institutions"]
    config_institutions_page()
    add_institution(table=table_institutions, engine=engine)


if __name__ == "__main__":
    institutions()

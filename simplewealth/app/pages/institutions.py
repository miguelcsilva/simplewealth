from itertools import chain

import sqlalchemy as sa
import streamlit as st

from simplewealth.app.validation import is_text_input_empty
from simplewealth.database import get_engine, get_metadata
from simplewealth.database.operations import execute, select
from simplewealth.database.queries.institutions import (
    get_delete_institution_query,
    get_insert_institution_query,
    get_select_all_institutions_query,
    get_update_institution_name_query,
)


def config_institutions_page() -> None:
    st.set_page_config(
        page_title="SimpleWealth - Institutions",
    )
    st.title("Institutions")


def get_all_institutions_name(engine: sa.Engine, table: sa.Table) -> list[str]:
    return list(
        chain(
            *select(
                engine=engine, statement=get_select_all_institutions_query(table=table)
            )
        )
    )


def add_institution_component(table: sa.Table, engine: sa.Engine) -> None:
    with st.container():
        st.header("Add")
        name = st.text_input(
            label="Name:",
        )
        if st.button(label="Add") and not is_text_input_empty(
            text=name, message="Cannot have an empty institution name."
        ):
            execute(
                engine=engine,
                statements=(get_insert_institution_query(table=table, name=name),),
            )


def update_institution_component(table: sa.Table, engine: sa.Engine) -> None:
    with st.container():
        st.header("Update")

        names = get_all_institutions_name(engine=engine, table=table)
        old_name = st.selectbox(label="Old name:", options=names)
        new_name = st.text_input(
            label="New name:",
        )
        if st.button(label="Update") and not is_text_input_empty(
            text=new_name, message="Cannot have an empty institution name."
        ):
            execute(
                engine=engine,
                statements=(
                    get_update_institution_name_query(
                        table=table, old_name=old_name, new_name=new_name
                    ),
                ),
            )
            st.experimental_rerun()


def delete_institution_component(table: sa.Table, engine: sa.Engine) -> None:
    with st.container():
        st.header("Delete")

        names = get_all_institutions_name(engine=engine, table=table)
        name = st.selectbox(label="Name:", options=names)
        if st.button(label="Delete"):
            execute(
                engine=engine,
                statements=(get_delete_institution_query(table=table, name=name),),
            )
            st.experimental_rerun()


def institutions() -> None:
    from simplewealth.settings import SETTINGS

    engine = get_engine(url=SETTINGS.DATABASE_URI)
    metadata = get_metadata(engine=engine)
    table_institutions = metadata.tables["institutions"]
    config_institutions_page()

    add_institution_component(table=table_institutions, engine=engine)
    update_institution_component(table=table_institutions, engine=engine)
    delete_institution_component(table=table_institutions, engine=engine)


if __name__ == "__main__":
    institutions()  # pragma: no cover

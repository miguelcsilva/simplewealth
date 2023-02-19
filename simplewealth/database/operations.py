from typing import Iterable

import sqlalchemy as sa


def insert(engine: sa.Engine, statements: Iterable[sa.Insert]) -> None:
    with engine.connect() as connection:
        for statement in statements:
            connection.execute(statement=statement)
        connection.commit()


def get_insert_operation_type_defaults_statement(table: sa.Table) -> sa.Insert:
    defaults: list[dict[str, str]] = [
        {"name": "purchase"},
        {"name": "sell"},
        {"name": "yield"},
    ]
    return sa.insert(table).values(defaults)


def get_insert_institution_statement(table: sa.Table, name: str) -> sa.Insert:
    values: list[dict[str, str]] = [{"name": name}]
    return sa.insert(table).values(values)

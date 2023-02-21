from typing import Any, Iterable

import sqlalchemy as sa


def execute(engine: sa.Engine, statements: Iterable[sa.Executable]) -> None:
    with engine.connect() as connection:
        for statement in statements:
            connection.execute(statement=statement)
        connection.commit()


def select(engine: sa.Engine, statement: sa.Select) -> list[tuple[Any, ...]]:
    with engine.connect() as connection:
        return connection.execute(statement=statement)

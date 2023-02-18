import sqlalchemy as sa

from simplewealth.database.initialization import define_operation_type_table
from simplewealth.database.operations import (
    get_insert_operation_type_defaults_statement,
)


def test_insert_defaults_in_table_operation_type() -> None:
    table = define_operation_type_table(metadata=sa.MetaData())
    statement = get_insert_operation_type_defaults_statement(table=table)
    assert statement.is_insert is True
    assert all(
        param in statement.compile().params.values()  # type: ignore[misc]
        for param in ("purchase", "sell", "yield")
    )

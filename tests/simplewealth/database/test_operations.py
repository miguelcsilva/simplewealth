from unittest.mock import patch

import sqlalchemy as sa


def test_insert_defaults_in_table_operation_type() -> None:
    with (
        patch("simplewealth.database.initialization.METADATA"),
        patch("simplewealth.database.initialization.ENGINE"),
    ):
        from simplewealth.database.initialization import define_operation_type_table
        from simplewealth.database.operations import (
            get_insert_operation_type_defaults_statement,
        )

        table = define_operation_type_table(metadata=sa.MetaData())
        statement = get_insert_operation_type_defaults_statement(table=table)
    assert statement.is_insert is True
    assert all(
        param in statement.compile().params.values()  # type: ignore[misc]
        for param in ("purchase", "sell", "yield")
    )

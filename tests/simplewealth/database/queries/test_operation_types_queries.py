import sqlalchemy as sa


def test_get_insert_operation_types_defaults_query() -> None:
    from simplewealth.database.initialization import define_operation_types_table
    from simplewealth.database.queries.operation_types import (
        get_insert_default_operation_types_query,
    )

    table = define_operation_types_table(metadata=sa.MetaData())
    query = get_insert_default_operation_types_query(table=table)
    assert query.is_insert is True
    assert all(
        param in query.compile().params.values()  # type: ignore[misc]
        for param in ("purchase", "sell", "yield")
    )

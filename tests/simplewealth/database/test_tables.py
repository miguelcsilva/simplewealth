import sqlalchemy as sa

from simplewealth.database.tables import (
    define_operation_type,
    insert_operation_type_defaults,
)


def test_define_operation_type_column_names() -> None:
    table = define_operation_type(metadata=sa.MetaData())
    assert all(
        # sqlalchemy Table.columns method returns type Column[Any]
        name in table.columns.keys()  # type: ignore[misc]
        for name in ("id", "name")
    )


def test_define_operation_type_column_types() -> None:
    table = define_operation_type(metadata=sa.MetaData())
    # sqlalchemy Table.columns method returns type Column[Any]
    assert type(table.columns.id.type) is sa.Integer  # type: ignore[misc]
    assert type(table.columns.name.type) is sa.String  # type: ignore[misc]


def test_insert_operation_type_defaults() -> None:
    table = define_operation_type(metadata=sa.MetaData())
    statement = insert_operation_type_defaults(table=table)
    assert statement.is_insert is True
    assert all(
        param in statement.compile().params.values()  # type: ignore[misc]
        for param in ("purchase", "sell", "yield")
    )

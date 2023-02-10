import sqlalchemy as sa

from simplewealth.database.tables.operation_type import define_table_operation_type


def test_define_table_operation_type_column_names() -> None:
    table = define_table_operation_type(metadata=sa.MetaData())
    assert all(
        # sqlalchemy Table.columns method returns type Column[Any]
        name in table.columns.keys()  # type: ignore[misc]
        for name in ("id", "name")
    )


def test_define_table_operation_type_column_types() -> None:
    table = define_table_operation_type(metadata=sa.MetaData())
    # sqlalchemy Table.columns method returns type Column[Any]
    assert type(table.columns.id.type) is sa.Integer  # type: ignore[misc]
    assert type(table.columns.name.type) is sa.String  # type: ignore[misc]

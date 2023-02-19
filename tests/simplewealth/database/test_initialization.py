from unittest.mock import patch

import sqlalchemy as sa


def test_insert_defaults_in_table_operation_type_column_names() -> None:
    with (
        patch("simplewealth.database.initialization.METADATA"),
        patch("simplewealth.database.initialization.ENGINE"),
    ):
        from simplewealth.database.initialization import define_operation_type_table

        table = define_operation_type_table(metadata=sa.MetaData())
    assert all(
        # sqlalchemy Table.columns method returns type Column[Any]
        name in table.columns.keys()  # type: ignore[misc]
        for name in ("id", "name")
    )


def test_insert_defaults_in_table_operation_type_column_types() -> None:
    with (
        patch("simplewealth.database.initialization.METADATA"),
        patch("simplewealth.database.initialization.ENGINE"),
    ):
        from simplewealth.database.initialization import define_operation_type_table

        table = define_operation_type_table(metadata=sa.MetaData())
    # sqlalchemy Table.columns method returns type Column[Any]
    assert type(table.columns.id.type) is sa.Integer  # type: ignore[misc]
    assert type(table.columns.name.type) is sa.String  # type: ignore[misc]


def test_create_database() -> None:
    with (
        patch("simplewealth.database.initialization.METADATA"),
        patch("simplewealth.database.initialization.ENGINE"),
        patch("sqlalchemy.MetaData.create_all") as patch_create_all,
        patch(
            "simplewealth.database.initialization.define_operation_type_table"
        ) as patch_define_table_operation_type,
    ):
        from simplewealth.database import create_database

        create_database(
            metadata=sa.MetaData(),
            engine=sa.create_engine(url="postgresql://test:test@testhost:1234/test"),
        )
    patch_define_table_operation_type.assert_called_once()
    patch_create_all.assert_called_once()

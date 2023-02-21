from unittest.mock import MagicMock, patch

import sqlalchemy as sa


def test_get_engine() -> None:
    with patch(
        "simplewealth.database.initialization.sa.create_engine"
    ) as mock_create_engine:
        from simplewealth.database.initialization import get_engine

        mock_database_uri = MagicMock()
        get_engine(url=mock_database_uri)
    mock_create_engine.assert_called_once_with(url=mock_database_uri)


def test_get_metadata() -> None:
    with patch(
        "simplewealth.database.initialization.sa.MetaData.reflect"
    ) as mock_metadata_reflect:
        from simplewealth.database.initialization import get_metadata

        mock_engine = MagicMock()
        get_metadata(engine=mock_engine)
    mock_metadata_reflect.assert_called_once_with(bind=mock_engine)


def test_insert_defaults_in_table_operation_types_column_names() -> None:
    from simplewealth.database.initialization import define_operation_types_table

    table = define_operation_types_table(metadata=sa.MetaData())
    assert all(
        # sqlalchemy Table.columns method returns type Column[Any]
        name in table.columns.keys()  # type: ignore[misc]
        for name in ("id", "name")
    )


def test_insert_defaults_in_table_operation_types_column_types() -> None:
    from simplewealth.database.initialization import define_operation_types_table

    table = define_operation_types_table(metadata=sa.MetaData())
    # sqlalchemy Table.columns method returns type Column[Any]
    assert type(table.columns.id.type) is sa.Integer  # type: ignore[misc]
    assert type(table.columns.name.type) is sa.String  # type: ignore[misc]


def test_create_database() -> None:
    with (
        patch(
            "simplewealth.database.initialization.define_operation_types_table"
        ) as mock_define_table_operation_types,
        patch(
            "simplewealth.database.initialization.define_institutions_table"
        ) as mock_define_institutions_table,
    ):
        from simplewealth.database import create_database

        mock_metadata, mock_engine = MagicMock(), MagicMock()
        with patch.object(mock_metadata, "create_all") as mock_metadata_create_all:
            create_database(metadata=mock_metadata, engine=mock_engine)
    mock_define_table_operation_types.assert_called_once_with(metadata=mock_metadata)
    mock_define_institutions_table.assert_called_once_with(metadata=mock_metadata)
    mock_metadata_create_all.assert_called_once_with(bind=mock_engine)

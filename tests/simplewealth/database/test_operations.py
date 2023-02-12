from unittest.mock import MagicMock, call, patch

from simplewealth.database import create_database, insert


def test_create_database() -> None:
    with (
        patch("sqlalchemy.MetaData.create_all") as patch_create_all,
        patch(
            "simplewealth.database.operations.define_operation_type"
        ) as patch_define_table_operation_type,
    ):
        database_uri = "postgresql://test:test@testhost:1234/test"
        create_database(database_uri=database_uri)
    patch_define_table_operation_type.assert_called_once()
    patch_create_all.assert_called_once()


def test_insert() -> None:
    connection_mock = MagicMock()
    execute_mock = MagicMock()
    commit_mock = MagicMock()
    connection_mock.execute = execute_mock
    connection_mock.commit = commit_mock

    insert(connection=connection_mock, statements=("a", "b"))  # type: ignore[arg-type]
    execute_mock.assert_has_calls(
        calls=(call(statement="a"), call(statement="b")), any_order=True
    )
    commit_mock.assert_called_once()

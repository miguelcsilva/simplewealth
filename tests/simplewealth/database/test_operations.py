from unittest.mock import MagicMock, call, patch

import sqlalchemy as sa


def test_insert() -> None:
    from simplewealth.database.operations import insert

    mock_engine, mock_statements = MagicMock(), [MagicMock() for _ in range(10)]
    execute_calls = [call(statement=statement) for statement in mock_statements]
    with patch.object(mock_engine, "connect") as mock_connection:
        mock_connection_return_value = MagicMock()
        mock_connection.return_value.__enter__.return_value = (  # type: ignore[misc]
            mock_connection_return_value
        )
        with (
            patch.object(
                mock_connection_return_value, "execute"
            ) as mock_connection_execute,
            patch.object(
                mock_connection_return_value, "commit"
            ) as mock_connection_commit,
        ):
            insert(engine=mock_engine, statements=mock_statements)
    mock_connection_execute.assert_has_calls(calls=execute_calls)
    mock_connection_commit.assert_called_once()


def test_get_insert_operation_type_defaults_statement() -> None:
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


def test_get_insert_institution_statement() -> None:
    from simplewealth.database.initialization import define_institutions_table
    from simplewealth.database.operations import get_insert_institution_statement

    table = define_institutions_table(metadata=sa.MetaData())
    statement = get_insert_institution_statement(table=table, name="test_name")
    assert statement.is_insert is True
    assert all(
        param in statement.compile().params.values()  # type: ignore[misc]
        for param in ("test_name",)
    )

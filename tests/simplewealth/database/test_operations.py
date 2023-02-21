from unittest.mock import MagicMock, call, patch


def test_execute() -> None:
    from simplewealth.database.operations import execute

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
            execute(engine=mock_engine, statements=mock_statements)
    mock_connection_execute.assert_has_calls(calls=execute_calls)
    mock_connection_commit.assert_called_once()

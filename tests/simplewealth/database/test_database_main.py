from unittest.mock import MagicMock, patch


def test_main() -> None:
    with (
        patch("simplewealth.database.main.get_engine") as mock_get_engine,
        patch("simplewealth.database.main.get_metadata") as mock_get_metadata,
        patch("simplewealth.database.main.create_database") as mock_create_database,
    ):
        from simplewealth.database.main import main

        mock_get_engine.return_value = MagicMock()
        mock_get_metadata.return_value = MagicMock()
        main()
    mock_create_database.assert_called_once_with(
        metadata=mock_get_metadata.return_value, engine=mock_get_engine.return_value
    )

from simplewealth.database.main import main
from unittest.mock import patch


def test_main():
    with (
        patch("simplewealth.database.main.METADATA") as mock_metadata,
        patch("simplewealth.database.main.ENGINE") as mock_engine,
        patch("simplewealth.database.main.create_database") as mock_create_database,
    ):
        main()
    mock_create_database.assert_called_once_with(metadata=mock_metadata, engine=mock_engine)

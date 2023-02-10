from unittest.mock import patch

from simplewealth.database import setup_database


def test_setup_database() -> None:
    with (
        patch("sqlalchemy.MetaData.create_all") as patch_create_all,
        patch(
            "simplewealth.database.initialize.define_table_operation_type"
        ) as patch_define_table_operation_type,
    ):
        database_uri = "postgresql://test:test@testhost:1234/test"
        setup_database(database_uri=database_uri)
    patch_define_table_operation_type.assert_called_once()
    patch_create_all.assert_called_once()

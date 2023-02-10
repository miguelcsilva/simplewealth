import sqlalchemy as sa

from .tables.operation_type import define_table_operation_type


def setup_database(database_uri: str) -> sa.MetaData:
    metadata = sa.MetaData()
    define_table_operation_type(metadata=metadata),

    metadata.create_all(bind=sa.create_engine(url=database_uri))
    return metadata

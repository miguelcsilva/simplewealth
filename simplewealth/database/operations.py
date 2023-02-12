import sqlalchemy as sa

from .tables import define_operation_type


def create_database(database_uri: str) -> tuple[sa.MetaData, sa.Engine]:
    metadata = sa.MetaData()
    engine = sa.create_engine(url=database_uri)

    define_operation_type(metadata=metadata)
    metadata.create_all(bind=engine)
    return metadata, engine


def insert(connection: sa.Connection, statements: tuple[sa.Insert, ...]) -> None:
    with connection:
        for statement in statements:
            connection.execute(statement=statement)
        connection.commit()

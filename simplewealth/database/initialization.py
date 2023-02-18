import sqlalchemy as sa

from ..settings import SETTINGS

ENGINE = sa.create_engine(url=SETTINGS.DATABASE_URI)
METADATA = sa.MetaData()
METADATA.reflect(bind=ENGINE)


def define_operation_type_table(metadata: sa.MetaData) -> sa.Table:
    return sa.Table(
        "operations_type",
        metadata,
        sa.Column(name="id", type_=sa.Integer, primary_key=True),
        sa.Column(name="name", type_=sa.String, nullable=False, unique=True),
    )


def define_institutions_table(metadata: sa.MetaData) -> sa.Table:
    return sa.Table(
        "institutions",
        metadata,
        sa.Column(name="id", type_=sa.Integer, primary_key=True),
        sa.Column(name="name", type_=sa.String, nullable=False, unique=True),
    )


def create_database(metadata: sa.MetaData, engine: sa.Engine) -> None:
    define_operation_type_table(metadata=metadata)
    define_institutions_table(metadata=metadata)
    metadata.create_all(bind=engine)

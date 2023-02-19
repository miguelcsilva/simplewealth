import sqlalchemy as sa


def get_engine(url: str) -> sa.Engine:
    return sa.create_engine(url=url)


def get_metadata(engine: sa.Engine) -> sa.MetaData:
    return sa.MetaData().reflect(bind=engine)


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

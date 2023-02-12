import sqlalchemy as sa


def define_operation_type(metadata: sa.MetaData) -> sa.Table:
    return sa.Table(
        "operation_type",
        metadata,
        sa.Column(name="id", type_=sa.Integer, primary_key=True),
        sa.Column(name="name", type_=sa.String, nullable=False, unique=True),
    )


def insert_operation_type_defaults(table: sa.Table) -> sa.Insert:
    defaults: list[dict[str, str]] = [
        {"name": "purchase"},
        {"name": "sell"},
        {"name": "yield"},
    ]
    return sa.insert(table).values(defaults)

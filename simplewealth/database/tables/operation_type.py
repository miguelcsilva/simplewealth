import sqlalchemy as sa


def define_table_operation_type(metadata: sa.MetaData) -> sa.Table:
    return sa.Table(
        "operation_type",
        metadata,
        sa.Column(name="id", type_=sa.Integer, primary_key=True),
        sa.Column(name="name", type_=sa.String, nullable=False, unique=True),
    )

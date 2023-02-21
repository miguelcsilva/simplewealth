import sqlalchemy as sa


def get_insert_default_operation_types_query(table: sa.Table) -> sa.Insert:
    defaults: list[dict[str, str]] = [
        {"name": "purchase"},
        {"name": "sell"},
        {"name": "yield"},
    ]
    return sa.insert(table).values(defaults)

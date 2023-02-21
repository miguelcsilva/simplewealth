import sqlalchemy as sa


def get_insert_institution_query(table: sa.Table, name: str) -> sa.Insert:
    values: list[dict[str, str]] = [{"name": name}]
    return sa.insert(table=table).values(values)


def get_select_all_institutions_query(table: sa.Table) -> sa.Select:
    return sa.select(table.columns.name)


def get_update_institution_name_query(
    table: sa.Table, old_name: str, new_name: str
) -> sa.Update:
    return (
        sa.update(table=table)
        .where(table.columns.name == old_name)
        .values(name=new_name)
    )


def get_delete_institution_query(table: sa.Table, name: str) -> sa.Update:
    return sa.delete(table=table).where(table.columns.name == name)

import sqlalchemy as sa


def test_get_insert_institution_query() -> None:
    from simplewealth.database.initialization import define_institutions_table
    from simplewealth.database.queries.institutions import get_insert_institution_query

    table = define_institutions_table(metadata=sa.MetaData())
    query = get_insert_institution_query(table=table, name="test_name")
    assert query.is_insert is True
    assert all(
        param in query.compile().params.values()  # type: ignore[misc]
        for param in ("test_name",)
    )

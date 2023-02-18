from simplewealth.database import ENGINE, METADATA, create_database

create_database(metadata=METADATA, engine=ENGINE)

from simplewealth.database import ENGINE, METADATA, create_database

def main() -> None:
    create_database(metadata=METADATA, engine=ENGINE)

if __name__ == "__main__":
    main() # pragma: no cover

from ..database import create_database, get_engine, get_metadata
from ..settings import SETTINGS


def main() -> None:
    engine = get_engine(url=SETTINGS.DATABASE_URI)
    metadata = get_metadata(engine=engine)
    create_database(metadata=metadata, engine=engine)


if __name__ == "__main__":
    main()  # pragma: no cover

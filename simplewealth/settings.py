from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseSettings

# https://github.com/pydantic/pydantic/issues/1490
if TYPE_CHECKING:  # pragma: no cover
    PostgresDsn = str
else:
    from pydantic import PostgresDsn


class Settings(BaseSettings):
    DATABASE_URI: PostgresDsn = (
        "postgresql://simplewealth:simplewealth@localhost:5432/simplewealth"
    )


def get_settings() -> Settings:
    return Settings()


SETTINGS = get_settings()

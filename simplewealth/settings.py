from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseSettings

# https://github.com/pydantic/pydantic/issues/1490
if TYPE_CHECKING:
    PostgresDsn = str
else:
    from pydantic import PostgresDsn


class Settings(BaseSettings):
    DATABASE_URI: PostgresDsn = (
        "postgres://simplewealth:simplewealth@localhost:5432/simplewealth"
    )


def get_settings() -> Settings:
    return Settings()

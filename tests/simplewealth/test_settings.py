from pytest import MonkeyPatch

from simplewealth.settings import get_settings


def test_Settings_default() -> None:
    SETTINGS = get_settings()
    assert (
        SETTINGS.DATABASE_URI
        == "postgresql://simplewealth:simplewealth@localhost:5432/simplewealth"
    )


def test_Settings_override(monkeypatch: MonkeyPatch) -> None:
    TEST_DATABASE_URI = "postgresql://test:test@testhost:1234/test"
    monkeypatch.setenv("DATABASE_URI", TEST_DATABASE_URI)
    SETTINGS = get_settings()
    assert SETTINGS.DATABASE_URI == TEST_DATABASE_URI

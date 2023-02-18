from unittest.mock import patch
from simplewealth.app.main import config_main_page, main

def test_config_main_page():
    with (
        patch("simplewealth.app.main.st.set_page_config") as mock_set_page_config,
        patch("simplewealth.app.main.st.title") as mock_title,
    ):
        config_main_page()
    mock_set_page_config.assert_called_once()
    mock_title.assert_called_once()

def test_main():
    with patch("simplewealth.app.main.config_main_page") as mock_config_main_page:
        main()
    mock_config_main_page.assert_called_once()

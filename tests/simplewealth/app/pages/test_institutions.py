from unittest.mock import patch
from simplewealth.app.pages.institutions import config_institutions_page, add_institution, submit_new_institution, institutions

def test_config_main_page():
    with (
        patch("simplewealth.app.pages.institutions.st.set_page_config") as mock_set_page_config,
        patch("simplewealth.app.pages.institutions.st.title") as mock_title,
    ):
        config_institutions_page()
    mock_set_page_config.assert_called_once()
    mock_title.assert_called_once()

def test_add_institution_not_pressed():
    with (
        patch("simplewealth.app.pages.institutions.st.text_input") as mock_text_input,
        patch("simplewealth.app.pages.institutions.st.button") as mock_button,
        patch("simplewealth.app.pages.institutions.submit_new_institution") as mock_submit_new_institution,
    ):
        mock_text_input.return_value = "test"
        mock_button.return_value = False
        add_institution()
    mock_submit_new_institution.assert_not_called()

def test_add_institution_pressed():
    with (
        patch("simplewealth.app.pages.institutions.st.text_input") as mock_text_input,
        patch("simplewealth.app.pages.institutions.st.button") as mock_button,
        patch("simplewealth.app.pages.institutions.submit_new_institution") as mock_submit_new_institution,
    ):
        mock_text_input.return_value = "test"
        mock_button.return_value = True
        add_institution()
    mock_submit_new_institution.assert_called_with(institution="test")

def test_submit_new_instituion():
    with (
        patch("simplewealth.app.pages.institutions.get_insert_institution_statement") as mock_get_insert_institution_statement,
        patch("simplewealth.app.pages.institutions.insert") as mock_insert,
        patch("simplewealth.app.pages.institutions.TABLE_INSTITUTIONS") as mock_table_institutions,
        patch("simplewealth.app.pages.institutions.ENGINE") as mock_engine,
    ):
        institution_name = "test"
        mock_table_institutions.return_value = "test_table_institutions"
        submit_new_institution(institution=institution_name)
    mock_get_insert_institution_statement.assert_called_once_with(
        table=mock_table_institutions,
        institution_name=institution_name
    )
    mock_insert.assert_called_once_with(engine=mock_engine, statements=(mock_get_insert_institution_statement.return_value,))

def test_institutions():
    with (
        patch("simplewealth.app.pages.institutions.config_institutions_page") as mock_config_institutions_page,
        patch("simplewealth.app.pages.institutions.add_institution") as mock_add_institution,
    ):
        institutions()
    mock_config_institutions_page.assert_called_once()
    mock_add_institution.assert_called_once()
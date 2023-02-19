from unittest.mock import MagicMock, patch


def test_config_main_page() -> None:
    with (
        patch(
            "simplewealth.app.pages.institutions.st.set_page_config"
        ) as mock_set_page_config,
        patch("simplewealth.app.pages.institutions.st.title") as mock_title,
    ):
        from simplewealth.app.pages.institutions import config_institutions_page

        config_institutions_page()
    mock_set_page_config.assert_called_once()
    mock_title.assert_called_once()


def test_add_institution_not_pressed() -> None:
    with (
        patch("simplewealth.app.pages.institutions.st.text_input") as mock_text_input,
        patch("simplewealth.app.pages.institutions.st.button") as mock_button,
        patch(
            "simplewealth.app.pages.institutions.submit_new_institution"
        ) as mock_submit_new_institution,
    ):
        mock_text_input.return_value = "test"
        mock_button.return_value = False
        from simplewealth.app.pages.institutions import add_institution

        add_institution(table=MagicMock(), engine=MagicMock())
    mock_submit_new_institution.assert_not_called()


def test_add_institution_pressed() -> None:
    with (
        patch("simplewealth.app.pages.institutions.st.text_input") as mock_text_input,
        patch("simplewealth.app.pages.institutions.st.button") as mock_button,
        patch(
            "simplewealth.app.pages.institutions.submit_new_institution"
        ) as mock_submit_new_institution,
    ):
        mock_text_input.return_value = "test"
        mock_button.return_value = True
        from simplewealth.app.pages.institutions import add_institution

        mock_table, mock_engine = MagicMock(), MagicMock()
        add_institution(table=mock_table, engine=mock_engine)
    mock_submit_new_institution.assert_called_with(
        name="test", table=mock_table, engine=mock_engine
    )


def test_submit_new_instituion() -> None:
    with (
        patch(
            "simplewealth.app.pages.institutions.get_insert_institution_statement"
        ) as mock_get_insert_institution_statement,
        patch("simplewealth.app.pages.institutions.insert") as mock_insert,
    ):
        institution_name = "test"
        mock_get_insert_institution_statement.return_value = MagicMock()
        from simplewealth.app.pages.institutions import submit_new_institution

        mock_table, mock_engine = MagicMock(), MagicMock()
        submit_new_institution(
            name=institution_name, table=mock_table, engine=mock_engine
        )
    mock_get_insert_institution_statement.assert_called_once_with(
        table=mock_table, name=institution_name
    )
    mock_insert.assert_called_once_with(
        engine=mock_engine,
        statements=(mock_get_insert_institution_statement.return_value,),
    )


def test_institutions() -> None:
    with (
        patch("simplewealth.app.pages.institutions.get_engine") as mock_get_engine,
        patch("simplewealth.app.pages.institutions.get_metadata") as mock_get_metadata,
        patch(
            "simplewealth.app.pages.institutions.config_institutions_page"
        ) as mock_config_institutions_page,
        patch(
            "simplewealth.app.pages.institutions.add_institution"
        ) as mock_add_institution,
    ):
        from simplewealth.app.pages.institutions import institutions

        institutions()
    mock_get_engine.assert_called_once()
    mock_get_metadata.assert_called_once()
    mock_config_institutions_page.assert_called_once()
    mock_add_institution.assert_called_once()

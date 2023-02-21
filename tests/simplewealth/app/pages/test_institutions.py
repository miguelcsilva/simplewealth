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


def test_add_institution_button_not_pressed() -> None:
    with (
        patch("simplewealth.app.pages.institutions.st.text_input") as mock_text_input,
        patch("simplewealth.app.pages.institutions.st.button") as mock_button,
        patch("simplewealth.app.pages.institutions.execute") as mock_execute,
    ):
        mock_text_input.return_value = "test"
        mock_button.return_value = False
        from simplewealth.app.pages.institutions import add_institution_component

        add_institution_component(table=MagicMock(), engine=MagicMock())
    mock_execute.assert_not_called()


def test_add_institution_button_pressed() -> None:
    with (
        patch("simplewealth.app.pages.institutions.st.text_input") as mock_text_input,
        patch("simplewealth.app.pages.institutions.st.button") as mock_button,
        patch(
            "simplewealth.app.pages.institutions.get_insert_institution_query"
        ) as mock_get_insert_institution_query,
        patch("simplewealth.app.pages.institutions.execute") as mock_execute,
    ):
        mock_text_input.return_value = "test"
        mock_button.return_value = True
        mock_insert_institution_query = MagicMock()
        mock_get_insert_institution_query.return_value = mock_insert_institution_query
        mock_table, mock_engine = MagicMock(), MagicMock()
        from simplewealth.app.pages.institutions import add_institution_component

        add_institution_component(table=mock_table, engine=mock_engine)
    mock_execute.assert_called_with(
        engine=mock_engine, statements=(mock_insert_institution_query,)
    )


def test_update_institution_button_not_pressed() -> None:
    with (
        patch("simplewealth.app.pages.institutions.st.text_input") as mock_text_input,
        patch("simplewealth.app.pages.institutions.st.selectbox") as mock_selectbox,
        patch("simplewealth.app.pages.institutions.st.button") as mock_button,
        patch("simplewealth.app.pages.institutions.execute") as mock_execute,
    ):
        mock_text_input.return_value = "text_input"
        mock_selectbox.return_value = "select_box"
        mock_button.return_value = False
        from simplewealth.app.pages.institutions import add_institution_component

        add_institution_component(table=MagicMock(), engine=MagicMock())
    mock_execute.assert_not_called()


def test_update_institution_button_pressed() -> None:
    with (
        patch("simplewealth.app.pages.institutions.st.text_input"),
        patch("simplewealth.app.pages.institutions.st.selectbox"),
        patch("simplewealth.app.pages.institutions.st.button") as mock_button,
        patch("simplewealth.app.pages.institutions.get_all_institutions_name"),
        patch(
            "simplewealth.app.pages.institutions.get_update_institution_name_query"
        ) as mock_get_update_institution_name_query,
        patch("simplewealth.app.pages.institutions.execute") as mock_execute,
        patch(
            "simplewealth.app.pages.institutions.st.experimental_rerun"
        ) as mock_experimental_rerun,
    ):
        mock_button.return_value = True
        mock_update_institution_name_query = MagicMock()
        mock_get_update_institution_name_query.return_value = (
            mock_update_institution_name_query
        )
        mock_table, mock_engine = MagicMock(), MagicMock()
        from simplewealth.app.pages.institutions import update_institution_component

        update_institution_component(table=mock_table, engine=mock_engine)
    mock_execute.assert_called_once_with(
        engine=mock_engine, statements=(mock_update_institution_name_query,)
    )
    mock_experimental_rerun.assert_called_once()


def test_delete_institution_button_not_pressed() -> None:
    with (
        patch("simplewealth.app.pages.institutions.st.selectbox"),
        patch("simplewealth.app.pages.institutions.st.button") as mock_button,
        patch("simplewealth.app.pages.institutions.get_all_institutions_name"),
        patch("simplewealth.app.pages.institutions.execute") as mock_execute,
    ):
        mock_button.return_value = False
        from simplewealth.app.pages.institutions import delete_institution_component

        delete_institution_component(table=MagicMock(), engine=MagicMock())
    mock_execute.assert_not_called()


def test_delete_institution_button_pressed() -> None:
    with (
        patch("simplewealth.app.pages.institutions.st.selectbox"),
        patch("simplewealth.app.pages.institutions.st.button") as mock_button,
        patch("simplewealth.app.pages.institutions.get_all_institutions_name"),
        patch(
            "simplewealth.app.pages.institutions.get_delete_institution_query"
        ) as mock_get_delete_institution_query,
        patch("simplewealth.app.pages.institutions.execute") as mock_execute,
        patch(
            "simplewealth.app.pages.institutions.st.experimental_rerun"
        ) as mock_experimental_rerun,
    ):
        mock_button.return_value = True
        mock_delete_institution_query = MagicMock()
        mock_get_delete_institution_query.return_value = mock_delete_institution_query
        mock_table, mock_engine = MagicMock(), MagicMock()
        from simplewealth.app.pages.institutions import delete_institution_component

        delete_institution_component(table=mock_table, engine=mock_engine)
    mock_execute.assert_called_once_with(
        engine=mock_engine, statements=(mock_delete_institution_query,)
    )
    mock_experimental_rerun.assert_called_once()


def test_institutions() -> None:
    with (
        patch("simplewealth.app.pages.institutions.get_engine") as mock_get_engine,
        patch("simplewealth.app.pages.institutions.get_metadata") as mock_get_metadata,
        patch(
            "simplewealth.app.pages.institutions.config_institutions_page"
        ) as mock_config_institutions_page,
        patch(
            "simplewealth.app.pages.institutions.add_institution_component"
        ) as mock_add_institution_component,
        patch(
            "simplewealth.app.pages.institutions.update_institution_component"
        ) as mock_update_institution_component,
        patch(
            "simplewealth.app.pages.institutions.delete_institution_component"
        ) as mock_delete_institution_component,
    ):
        from simplewealth.app.pages.institutions import institutions

        institutions()
    mock_get_engine.assert_called_once()
    mock_get_metadata.assert_called_once()
    mock_config_institutions_page.assert_called_once()
    mock_add_institution_component.assert_called_once()
    mock_update_institution_component.assert_called_once()
    mock_delete_institution_component.assert_called_once()

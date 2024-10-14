import pytest
from playwright.sync_api import Page

from src.pages.practice_pages.simple_elements.with_ids_page import WithIdsPage


@pytest.mark.with_ids
def test_label_txt(with_ids_page) -> None:
    # Visit Simple Elements page with ids
    with_ids_page.visit()

    # Get the label element text
    text = with_ids_page.get_label_txt()
    # Assert text equals: Some text for label
    assert "Some text for label" == text, f"Label text not match:\n Label: '{text}'"


@pytest.mark.with_ids
def test_push_button(with_ids_page) -> None:
    # Visit Simple Element page with ids
    with_ids_page.visit()

    # Click the button and verify the result
    with_ids_page.click_on_click_me_btn()


@pytest.mark.with_ids
def test_select_checkbox(with_ids_page) -> None:
    # Visit Simple Elements page with ids
    with_ids_page.visit()

    # Select checkbox
    with_ids_page.select_checkbox()

    # Deselect checkbox
    with_ids_page.deselect_checkbox()


@pytest.mark.with_ids
@pytest.mark.parametrize("button_no", [1, 2, 3])
def test_radio_buttons(with_ids_page, button_no) -> None:
    # Visit Simple Element page with ids
    with_ids_page.visit()

    # Click on radio button an verify it's clicked
    with_ids_page.check_radio_no(button_no)


@pytest.mark.with_ids
def test_input_field(with_ids_page) -> None:
    # Visit Simple Element page with ids
    with_ids_page.visit()

    # Fill in the input field with "test" and verify the result
    with_ids_page.fill_in_input_value("test")


@pytest.mark.with_ids
def test_text_area(with_ids_page) -> None:
    # Visit Simple Element page with ids
    with_ids_page.visit()

    # Fill in the text area and verify the result field fill_in_input_value
    with_ids_page.fill_in_text_area("Test\nTest2")


@pytest.mark.with_ids
@pytest.mark.parametrize("option_value", ["option1", "option2", "option3"])
def test_select_option_in_dropdown(with_ids_page, option_value) -> None:
    # Visit Simple Element page with ids
    with_ids_page.visit()

    # select option: option2 and verify result field value
    with_ids_page.select_dd_option(option_value)


@pytest.mark.with_ids
@pytest.mark.parametrize("slider_value", [1, 100, 55])
def test_slider_item(with_ids_page, slider_value) -> None:
    # Visit Simple Elements page with ids
    with_ids_page.visit()

    # Set a slider value and verify the result
    with_ids_page.set_slider_value(slider_value)


@pytest.mark.with_ids
def test_hover_over_label(with_ids_page) -> None:
    # Visit Simple Elements page with ids
    with_ids_page.visit()

    # Hover over label and verify results
    with_ids_page.hover_over_hover_label()


@pytest.mark.with_ids
@pytest.mark.parametrize("test_date", ["1900-01-01", "2024-06-15", "2300-12-31"])
def test_date_change(with_ids_page, test_date) -> None:
    # Visit Simple Elements with ids page
    with_ids_page.visit()

    # Set date and verify the result
    with_ids_page.set_date(test_date)

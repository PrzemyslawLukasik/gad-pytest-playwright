import pytest

from src.pages.practice_pages.simple_elements.no_ids_page import NoIdsPage


@pytest.mark.no_ids
def test_get_label_by_class(no_ids_page: NoIdsPage) -> None:
    no_ids_page.visit()
    no_ids_page.verify_label_text_by_class("Some text for label")


@pytest.mark.no_ids
def test_get_label_by_css(no_ids_page: NoIdsPage) -> None:
    no_ids_page.visit()
    no_ids_page.verify_label_text_by_css_cust_attr("Some text for label")

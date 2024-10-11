import pytest
from playwright.sync_api import Page


@pytest.mark.with_ids
def test_label_txt(with_ids_page) -> None:
    # Visit Simple Elements page with ids
    with_ids_page.visit()

    # Get the label element text
    text = with_ids_page.get_label_txt()
    # Assert text equals: Some text for label
    assert "Some text for label" == text, f"Label text not match:\n Label: '{text}'"

import pytest
from playwright.sync_api import Page


@pytest.mark.disabled
def test_click_button(not_present_disabled: Page) -> None:
    not_present_disabled.visit()
    not_present_disabled.click_me_button_click()


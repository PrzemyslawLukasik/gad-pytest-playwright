from dataclasses import dataclass

from playwright.sync_api import Locator, Page


@dataclass
class WithIdsPageLocators:
    """
    Simple elements page with ids on all elements.

    Id and data-testid are available.
    """

    def __init__(self, page: Page) -> None:
        self.page = page
        self.url = "/practice/simple-elements.html"

    def label(self) -> Locator:
        return self.page.get_by_test_id("dti-label-element")

    def click_me_button(self) -> Locator:
        return self.page.get_by_test_id("dti-button-element")

    def results_value(self) -> Locator:
        return self.page.get_by_test_id("dti-results")

    def results_container(self) -> Locator:
        return self.page.locator("#results-container")

    def checkbox_input(self) -> Locator:
        return self.page.get_by_test_id("dti-checkbox")

    def radio_btn_1(self) -> Locator:
        return self.page.get_by_test_id("dti-radio1")

    def radio_btn_2(self) -> Locator:
        return self.page.get_by_test_id("dti-radio2")

    def radio_btn_3(self) -> Locator:
        return self.page.get_by_test_id("dti-radio3")

    def slider(self) -> Locator:
        return self.page.get_by_test_id("dti-range")

    def input_field(self) -> Locator:
        return self.page.get_by_test_id("dti-input")

    def text_area(self) -> Locator:
        return self.page.get_by_test_id("dti-textarea")

    def droprown_menu(self) -> Locator:
        return self.page.get_by_test_id("dti-dropdown")

    def hover_label(self) -> Locator:
        return self.page.get_by_test_id("dti-tooltip-element")

    def date_field(self) -> Locator:
        return self.page.get_by_test_id("dti-date")

    def color_pick(self) -> Locator:
        return self.page.get_by_test_id("dti-color")

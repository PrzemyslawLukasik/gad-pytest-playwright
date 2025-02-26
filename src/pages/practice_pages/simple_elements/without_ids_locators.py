from dataclasses import dataclass

from playwright.sync_api import Locator, Page


@dataclass
class WithoutIdsLocators:
    """
    Simple elements page with ids on all elements.

    Id and data-testid are available.
    """

    def __init__(self, page: Page) -> None:
        self.page = page
        self.url = "/practice/simple-elements-no-ids.html"

    def label(self) -> Locator:
        return self.page.get_by_text("Some text for label")

    def click_me_button(self) -> Locator:
        return self.page.get_by_role("button", name="Click me!")

    def results_value(self) -> Locator:
        return self.page.get_by_test_id("dti-results")

    def results_container(self) -> Locator:
        return self.page.locator("#results-container")

    def checkbox_input(self) -> Locator:
        return self.page.get_by_role("checkbox")

    def radio_btn_1(self) -> Locator:
        return self.page.get_by_role("radio").first

    def radio_btn_2(self) -> Locator:
        return self.page.get_by_role("radio").nth(1)

    def radio_btn_3(self) -> Locator:
        return self.page.get_by_role("radio").nth(2)

    def slider(self) -> Locator:
        return self.page.get_by_role("slider")

    def input_field(self) -> Locator:
        return self.page.locator('input[type="text"]')

    def text_area(self) -> Locator:
        return self.page.locator("textarea")

    def droprown_menu(self) -> Locator:
        return self.page.get_by_role("combobox")

    def hover_label(self) -> Locator:
        return self.page.get_by_text("Hoover mouse here!")

    def date_field(self) -> Locator:
        return self.page.locator('input[type="date"]')

    def color_pick(self) -> Locator:
        return self.page.locator('input[type="color"]')

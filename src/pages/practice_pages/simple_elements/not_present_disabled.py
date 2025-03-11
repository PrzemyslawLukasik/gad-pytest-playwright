from dataclasses import dataclass

from playwright.sync_api import Page, Locator, expect

from src.pages.base_page import BasePage


@dataclass
class NotPresentDisabledLocators:
    def __init__(self, page: Page) -> None:
        self.page = page

    def click_me_button(self) -> Locator:
        return self.page.get_by_test_id("dti-button-element")

    def checkbox(self) -> Locator:
        return self.page.get_by_test_id("dti-checkbox")

    def input_field(self) -> Locator:
        return self.page.get_by_test_id("dti-input")

    def textarea_field(self) -> Locator:
        return self.page.get_by_test_id("dti-textarea")

    def result_field(self) -> Locator:
        return self.page.locator("#results-container")

    def result_value(self) -> Locator:
        return self.page.get_by_test_id("dti-results")


class NotPresentDisabled(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.url = "/practice/not-present-disabled-elements-1.html"
        self.locators = NotPresentDisabledLocators(self.page)

    def visit(self) -> None:
        self._visit(self.url)
        expect(self.page).to_have_title(
            "🦎 GAD - Different elements - from not present to enabled")

    def click_me_button_click(self) -> None:
        expect(self.locators.click_me_button()).to_be_visible(timeout=5000)
        expect(self.locators.click_me_button()).to_be_enabled(timeout=5000)
        self.locators.click_me_button().click()
        self.locators.result_field().scroll_into_view_if_needed()
        expect(self.locators.result_value()).to_have_text("You clicked the button!")

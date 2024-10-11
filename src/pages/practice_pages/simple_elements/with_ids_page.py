from dataclasses import dataclass

from playwright.sync_api import Locator, Page, expect

from src.pages.base_page import BasePage


@dataclass
class WithIdsPageLocators:
    """
    Simple elements page with ids on all elements.

    Id and data-testid are available.
    """

    def __init__(self, page: Page) -> None:
        self.page = page

    def label(self) -> Locator:
        return self.page.get_by_test_id("dti-label-element")

    def click_me_button(self) -> Locator:
        return self.page.get_by_test_id("dti-button-element")

    def results_value(self) -> Locator:
        return self.page.get_by_test_id("dti-results")

    def results_container(self) -> Locator:
        return self.page.locator("#results-container")


class WithIdsPage(BasePage):
    """
    Simple elements page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = WithIdsPageLocators(self.page)

        self.url = "/practice/simple-elements.html"

    def visit(self) -> None:
        self._visit(self.url)
        expect(self.locators.results_container()).to_be_visible()

    def get_label_txt(self) -> str:
        return self.locators.label().inner_text()

    def click_on_click_me_btn(self) -> None:
        self.locators.click_me_button().click()
        expect(self.locators.results_value()).to_have_text("You clicked the button!")

from dataclasses import dataclass

from playwright.sync_api import Locator, Page, expect

from src.pages.base_page import BasePage


@dataclass
class NoIdsLocators:
    def __init__(self, page: Page) -> None:
        self.page = page

    def label_by_class(self) -> Locator:
        return self.page.locator("label.my-label")

    def label_by_css_cust_attr(self) -> Locator:
        return self.page.locator('[custom-attribute="custom-value"]')

    def results_value(self) -> Locator:
        return self.page.get_by_test_id("dti-results")

    def results_container(self) -> Locator:
        return self.page.locator("#results-container")

    def click_me_button(self) -> Locator:
        return self.page.get_by_role("button", name="Click me!")

    def checkbox(self) -> Locator:
        return self.page.get_by_role("checkbox")


class NoIdsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.url = "/practice/simple-elements-no-ids.html"
        self.locators = NoIdsLocators(self.page)

    def visit(self) -> None:
        """
        Open page
        """
        self._visit(self.url)
        expect(self.locators.results_container()).to_be_visible()

    def verify_label_text_by_class(self, text: str) -> None:
        expect(self.locators.label_by_class()).to_have_text(text)

    def verify_label_text_by_css_cust_attr(self, text: str) -> None:
        expect(self.locators.label_by_css_cust_attr()).to_have_text(text)

    def click_on_click_me_button(self) -> None:
        expect(self.locators.click_me_button()).not_to_be_visible()
        self.locators.click_me_button().click()
        expect(self.locators.results_value()).to_have_text("You clicked the button!")

    def _is_checkbox_selected(self) -> bool:
        return True if self.locators.checkbox().is_checked() else False

    def click_checkbox(self, select: bool = True) -> None:
        if not self.locators.checkbox().is_checked() and select is True:
            self.locators.checkbox().click()
            expect(self.locators.checkbox()).to_be_checked()
        elif self.locators.checkbox().is_checked() and select is False:
            self.locators.checkbox().click()
            expect(self.locators.checkbox()).not_to_be_checked()

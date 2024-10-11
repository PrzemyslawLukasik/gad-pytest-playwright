from dataclasses import dataclass

from playwright.sync_api import Locator, Page, expect

from src.pages.base_page import BasePage


@dataclass
class PracticePageLocators:
    """
    Practice page locators
    """

    def __init__(self, page: Page) -> None:
        self.page = page

    def heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Practice your test automation")

    # Simple Elements

    def with_ids_btn(self) -> Locator:
        return self.page.get_by_role("button", name="With IDs")

    def without_ids_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Without IDs")

    def custom_attribute_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Custome attribute")

    def multiple_elements_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Multiple elements")

    # Elements with different state

    def disabled_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Disabled")

    def not_displayed_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Not Displayed")

    def not_present_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Not present")

    def not_present_to_enabled_btn(self) -> Locator:
        return self.page.get_by_role(
            "button", name="Not present -> enabled", exact=True
        )


class PracticePage(BasePage):
    """
    Parcice Page class
    """

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.url = "/practice"
        self.simple_elements_url = self.url + "/simple-elements.html"

        self.locators = PracticePageLocators(page)

    def is_practice_page_opened(self) -> bool:
        return True if self.locators.heading().is_visible() else False

    # Simple Elements

    def click_on_with_ids_btn(self) -> None:
        self.locators.with_ids_btn().click()
        expect(self.page).to_have_url(self.simple_elements_url)

    def click_on_without_ids_btn(self) -> None:
        self.locators.without_ids_btn().click()
        expect(self.page).to_have_url(self.simple_elements_url)

    def click_on_custom_attribut_btn(self) -> None:
        self.locators.custom_attribute_btn().click()
        expect(self.page).to_have_url(self.simple_elements_url)

    def click_on_multiple_elements_btn(self) -> None:
        self.locators.multiple_elements_btn().click()
        expect(self.page).to_have_url(self.simple_elements_url)

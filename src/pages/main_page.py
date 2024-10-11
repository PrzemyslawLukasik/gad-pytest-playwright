from dataclasses import dataclass

from playwright.sync_api import Locator, Page, expect

from src.pages.base_page import BasePage


class MainPageLocators:
    """
    Main Page Locators class

    All the locators are in method shape to unified them.
    """

    def __init__(self, page: Page):
        self.page = page

    def lets_start_btn_locator(self) -> Locator:
        return self.page.get_by_role("button", name="Let's start!")

    def practice_page_btn_locator(self) -> Locator:
        return self.page.get_by_role("button", name="Practice pages")


class MainPage(BasePage):
    """
    Main page class
    """

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.url = "/"
        self.locators = MainPageLocators(self.page)

    def visit(self) -> None:
        self._visit(self.url)
        expect(self.locators.practice_page_btn_locator()).to_be_visible()

    def click_on_practice_pages_btn(self) -> None:
        self.locators.practice_page_btn_locator().click()

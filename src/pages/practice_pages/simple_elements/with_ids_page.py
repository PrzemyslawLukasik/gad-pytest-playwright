import re
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


class WithIdsPage(BasePage):
    """
    Simple elements page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = WithIdsPageLocators(self.page)

        self.url = "/practice/simple-elements.html"

    def visit(self) -> None:
        """
        Open page
        """
        self._visit(self.url)
        expect(self.locators.results_container()).to_be_visible()

    def get_label_txt(self) -> str:
        """
        Get The label text
        """
        return self.locators.label().inner_text()

    def click_on_click_me_btn(self) -> None:
        self.locators.click_me_button().click()
        expect(self.locators.results_value()).to_have_text("You clicked the button!")

    def is_checkbox_selected(self) -> bool:
        return True if self.locators.checkbox_input().is_checked() else False

    def select_checkbox(self) -> None:
        if not self.is_checkbox_selected():
            self.locators.checkbox_input().click()
            expect(self.locators.results_value()).to_have_text("Checkbox is checked!")

    def deselect_checkbox(self) -> None:
        if self.is_checkbox_selected():
            self.locators.checkbox_input().click()
            self.locators.checkbox_input().scroll_into_view_if_needed()
            expect(self.locators.results_value()).to_have_text("Checkbox is unchecked!")

    def check_radio_no(self, no: int) -> None:
        self.locators.__getattribute__(f"radio_btn_{no}")().click()
        expect(self.locators.results_value()).to_have_text(
            f"Radio Button {no} clicked!"
        )

    def check_radio_btn_1(self) -> None:
        self.check_radio_no(1)

    def check_radio_btn_2(self) -> None:
        self.check_radio_no(2)

    def check_radio_btn_3(self) -> None:
        self.check_radio_no(3)

    def fill_in_input_value(self, text: str) -> None:
        self.locators.input_field().fill(text)
        self.locators.input_field().press("Enter")
        self.locators.results_value().scroll_into_view_if_needed()
        expect(self.locators.results_value()).to_have_text(
            "Input value changed to: " + text
        )

    def fill_in_text_area(self, text: str) -> None:
        self.locators.text_area().fill(text)
        self.locators.text_area().press("Tab")
        expect(self.locators.results_value()).to_have_text(
            "Textarea value changed to: " + text
        )

    def select_dd_option(self, option: str) -> None:
        self.locators.droprown_menu().click()
        self.locators.droprown_menu().select_option(value=option)
        self.locators.droprown_menu().scroll_into_view_if_needed()
        expect(self.locators.results_value()).to_have_text("Selected option: " + option)

    def set_slider_value(self, value: int) -> None:
        self.locators.slider().fill(str(value))
        self.locators.results_value().scroll_into_view_if_needed()
        expect(self.locators.results_value()).to_have_text(
            "Range value changed to: " + str(value)
        )

    def hover_over_hover_label(self) -> None:
        self.locators.results_container().scroll_into_view_if_needed()
        self.locators.hover_label().hover()
        expect(self.locators.results_value()).to_have_text("Mouse over event occurred!")

    def set_date(self, date: str) -> None:
        """
        Date has to be a string in format: ddmmyyyy
        """
        self.locators.results_container().scroll_into_view_if_needed()
        self.locators.date_field().fill(date)
        self.locators.date_field().press("Tab")
        expect(self.locators.results_value()).to_have_text("Selected date: " + date)

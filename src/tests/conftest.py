from typing import Generator

import pytest
from playwright.sync_api import Page

from src.pages.main_page import MainPage
from src.pages.practice_pages.practice_page import PracticePage
from src.pages.practice_pages.simple_elements.simple_elements_actions import (
    SimpleElementsActions,
)
from src.pages.practice_pages.simple_elements.with_ids_locators import (
    WithIdsPageLocators,
)
from src.pages.practice_pages.simple_elements.without_ids_locators import (
    WithoutIdsLocators,
)


@pytest.fixture
def main_page(page: Page) -> Generator[MainPage, None, None]:
    main_page = MainPage(page)
    yield main_page


@pytest.fixture
def practice_page(page: Page) -> Generator[PracticePage, None, None]:
    practice_page = PracticePage(page)
    yield practice_page


@pytest.fixture
def with_ids_actions(
    page: Page,
) -> Generator[SimpleElementsActions, None, None]:
    with_ids_page_locators = WithIdsPageLocators(page)
    with_ids_actions = SimpleElementsActions(page, with_ids_page_locators)
    yield with_ids_actions


@pytest.fixture
def without_ids_actions(
    page: Page,
) -> Generator[SimpleElementsActions, None, None]:
    without_ids_locators = WithoutIdsLocators(page)
    without_ids_actions = SimpleElementsActions(page, without_ids_locators)
    yield without_ids_actions

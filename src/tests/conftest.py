from typing import Generator

import pytest
from playwright.sync_api import Page

from src.pages.main_page import MainPage
from src.pages.practice_pages.practice_page import PracticePage
from src.pages.practice_pages.simple_elements.with_ids_page import WithIdsPage


@pytest.fixture
def main_page(page: Page) -> Generator[MainPage, None, None]:
    main_page = MainPage(page)
    yield main_page


@pytest.fixture
def practice_page(page: Page) -> Generator[PracticePage, None, None]:
    practice_page = PracticePage(page)
    yield practice_page


@pytest.fixture
def with_ids_page(page: Page) -> Generator[WithIdsPage, None, None]:
    with_ids_page = WithIdsPage(page)
    yield with_ids_page

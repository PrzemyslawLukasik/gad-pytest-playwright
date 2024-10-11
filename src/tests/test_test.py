from playwright.sync_api import Page


def test_test1(page: Page) -> None:
    page.goto("")


def test_locators(page: Page, main_page, practice_page, with_ids_page) -> None:
    # Pre-Conditions

    main_page.visit()
    main_page.click_on_practice_pages_btn()

    practice_page.click_on_with_ids_btn()
    with_ids_page.click_on_click_me_btn()

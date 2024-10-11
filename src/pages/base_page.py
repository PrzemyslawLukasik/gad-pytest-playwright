from playwright.sync_api import Page


class BasePage:
    """
    Base Page class
    """

    def __init__(self, page: Page):
        self.page = page
        self.url = "/"

    def _visit(self, url: str) -> None:
        self.page.goto(self.url)

from playwright.sync_api import Page, expect


class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(f'{self.base_url}{self.page_url}', wait_until='domcontentloaded')

    def find(self, locator):
        return self.page.locator(locator)

    def assert_open(self, text):
        expect(self.page).to_have_url(text)

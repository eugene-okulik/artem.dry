from playwright.sync_api import expect
from test_UI_adryamin.pages.base_page import BasePage


customizable_desk_loc = 'text=Customizable Desk'
products_breadcrumb_loc = '//ol[contains(@class, "breadcrumb")]//a[@href="/shop"]'
category_title_loc = 'span.d-inline-block'


class DesksPage(BasePage):
    page_url = '/shop/category/desks-1'

    def clic_customizable_desk(self):
        self.find(customizable_desk_loc).click()

    def clic_products_breadcrumb(self):
        self.find(products_breadcrumb_loc).click()

    def assert_category_title(self, expected_title):
        expect(self.find(category_title_loc)).to_have_text(expected_title)

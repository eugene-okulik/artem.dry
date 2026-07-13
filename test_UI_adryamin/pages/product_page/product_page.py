from test_UI_adryamin.pages.base_page import BasePage
from playwright.sync_api import expect

all_products_breadcrumb_loc = 'text=All Products'
multimedia_breadcrumb_loc = 'text=Multimedia'
product_title_loc = 'h1[itemprop="name"]'


class ProductPage(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def clic_all_products_breadcrumb(self):
        self.find(all_products_breadcrumb_loc).click()

    def clic_multimedia_breadcrumb(self):
        self.find(multimedia_breadcrumb_loc).click()

    def assert_product_title(self, expected_title):
        expect(self.find(product_title_loc)).to_have_text(expected_title)

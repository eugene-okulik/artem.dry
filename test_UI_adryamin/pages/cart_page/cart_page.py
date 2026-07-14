from playwright.sync_api import expect
from test_UI_adryamin.pages.base_page import BasePage


empty_cart_loc = '.js_cart_lines'
order_overview_loc = '.o_website_sale_checkout h3'
checkout_block_loc = '.o_website_sale_checkout'


class CartPage(BasePage):
    page_url = '/shop/cart'

    def assert_empty_cart_message(self, expected_message):
        expect(self.find(empty_cart_loc)).to_have_text(expected_message)

    def assert_order_overview_title(self, expected_title):
        expect(self.find(order_overview_loc)).to_have_text(expected_title)

    def assert_checkout_block(self):
        expect(self.find(f'{checkout_block_loc} .o_disabled').first).to_be_visible()

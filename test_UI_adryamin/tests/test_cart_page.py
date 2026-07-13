class TestCartPage:
    def test_empty_cart_message(self, cart_page):
        cart_page.open_page()
        cart_page.assert_empty_cart_message("Your cart is empty!")

    def test_order_overview_title(self, cart_page):
        cart_page.open_page()
        cart_page.assert_order_overview_title("Order overview")

    def test_checkout_block(self, cart_page):
        cart_page.open_page()
        cart_page.assert_checkout_block()

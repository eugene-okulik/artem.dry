class TestProductPage:
    def test_all_products_breadcrumb(self, product_page):
        product_page.open_page()
        product_page.clic_all_products_breadcrumb()
        product_page.assert_open("http://testshop.qa-practice.com/shop")

    def test_multimedia_breadcrumb(self, product_page):
        product_page.open_page()
        product_page.clic_multimedia_breadcrumb()
        product_page.assert_open("http://testshop.qa-practice.com/shop/category/multimedia-9")

    def test_product_title(self, product_page):
        product_page.open_page()
        product_page.assert_product_title("Office Design Software")

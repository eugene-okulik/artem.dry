class TestDesksPage:
    def test_open_product_from_catalog(self, desks_page):
        desks_page.open_page()
        desks_page.clic_customizable_desk()
        desks_page.assert_open("http://testshop.qa-practice.com/shop/customizable-desk-9?category=1")

    def test_products_breadcrumb(self, desks_page):
        desks_page.open_page()
        desks_page.clic_products_breadcrumb()
        desks_page.assert_open("http://testshop.qa-practice.com/shop")

    def test_desks_category_title(self, desks_page):
        desks_page.open_page()
        desks_page.assert_category_title("Desks")

import pytest
from test_UI_adryamin.pages.cart_page.cart_page import CartPage
from test_UI_adryamin.pages.desks_page.desks_page import DesksPage
from test_UI_adryamin.pages.product_page.product_page import ProductPage


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def desks_page(page):
    return DesksPage(page)


@pytest.fixture
def product_page(page):
    return ProductPage(page)

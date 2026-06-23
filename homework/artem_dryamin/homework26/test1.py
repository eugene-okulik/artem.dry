from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test1(driver):
    driver.get('http://testshop.qa-practice.com/')
    product = driver.find_element(By.CSS_SELECTOR, '[alt="Customizable Desk"]')
    ActionChains(driver).key_down(Keys.COMMAND).click(product).key_up(Keys.COMMAND).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.find_element(By.ID, 'add_to_cart').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[text()="Continue Shopping"]'))
    ).click()
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.CSS_SELECTOR, 'sup.my_cart_quantity').text == '1'
    )
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.CSS_SELECTOR, "a[href='/shop/cart']").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Customizable Desk')]")
    ))
    text = driver.find_element(By.XPATH, "//*[contains(text(), 'Customizable Desk')]").text
    assert "Customizable Desk" in text


def test2(driver):
    driver.get('http://testshop.qa-practice.com/')
    product = driver.find_element(By.CSS_SELECTOR, '[alt="Customizable Desk"]')
    card = product.find_element(By.XPATH, './ancestor::form')
    ActionChains(driver).move_to_element(product).perform()
    card.find_element(By.CSS_SELECTOR, 'a.a-submit').click()
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal-content'))
    )
    assert 'Customizable Desk' in modal.text

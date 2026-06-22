from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_1(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    dropdown = driver.find_element(By.CSS_SELECTOR, "[name='choose_language']")
    select = Select(dropdown)
    select.select_by_index(1)
    select_text = select.first_selected_option.text

    submit_button = driver.find_element(By.CSS_SELECTOR, "[name='submit']")
    submit_button.click()

    result = driver.find_element(By.CSS_SELECTOR, "#result-text")
    assert result.text == select_text


def test_2(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.XPATH, "//*[text()='Start']")
    start_button.click()
    finish_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='finish']")))
    assert finish_button.text == "Hello World!"

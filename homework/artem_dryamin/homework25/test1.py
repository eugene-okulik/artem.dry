from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get('https://www.qa-practice.com/elements/input/simple')
button_input = driver.find_element(By.CSS_SELECTOR, "[placeholder='Submit me']")
button_input.send_keys('test_input')
button_input.send_keys(Keys.ENTER)
result = driver.find_element(By.XPATH, "//*[@id='result-text']")
print(result.text)

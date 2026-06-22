from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.set_window_size(1024, 768)
driver.get('https://demoqa.com/automation-practice-form')

first_name = driver.find_element(By.CSS_SELECTOR, "[placeholder='First Name']")
last_name = driver.find_element(By.CSS_SELECTOR, "[placeholder='Last Name']")
email = driver.find_element(By.CSS_SELECTOR, "#userEmail")
gender = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
mobile_number = driver.find_element(By.CSS_SELECTOR, "[placeholder='Mobile Number']")
date_of_birth = driver.find_element(By.CSS_SELECTOR, "#dateOfBirthInput")
subjects_input = driver.find_element(By.CSS_SELECTOR, "#subjectsInput")
hobbies = driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
current_address = driver.find_element(By.XPATH, "//*[@placeholder='Current Address']")

first_name.send_keys('Artem')
last_name.send_keys('Dryamin')
email.send_keys('catdog@mail.ru')
gender.click()
driver.execute_script("window.scrollBy(0, 1000);")
mobile_number.send_keys('1234567810')

date_of_birth.click()
Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")).select_by_visible_text("June")
Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")).select_by_visible_text("2026")
driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--001:not(.react-datepicker__day--outside-month)").click()
date_of_birth.send_keys(Keys.ESCAPE)

subjects_input.send_keys("English")
subjects_input.send_keys(Keys.ENTER)

hobbies.click()
current_address.send_keys('Moscow')

select_state_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-select-3-input")))
select_state_input.send_keys("NCR")
select_state_input.send_keys(Keys.ENTER)

select_city_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-select-4-input")))
select_city_input.send_keys("Delhi")
select_city_input.send_keys(Keys.ENTER)

submit_button = wait.until(EC.presence_of_element_located((By.ID, "submit")))
driver.execute_script("arguments[0].click();", submit_button)

rows = wait.until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".table-responsive tbody tr"))
)

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) == 2:
        print(f"{cells[0].text}: {cells[1].text}")

driver.quit()

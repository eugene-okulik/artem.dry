from playwright.sync_api import Page


def test_1(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('Artem')
    page.get_by_role('textbox', name='password').fill('qwerty')
    page.get_by_role('button', name='Login').click()


def test_2(page: Page):
    data_birth_day = page.locator("//input[@id='dateOfBirthInput']")
    select_1 = page.locator("//*[@id='react-select-3-input']")
    select_2 = page.locator("//*[@id='react-select-4-input']")
    subject = page.locator('#subjectsInput')
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill("Artem")
    page.get_by_placeholder('Last name').fill('Dryamin')
    page.get_by_placeholder('name@example.com').fill('sobakusaka@yandex.ru')
    page.locator("//input[@id ='gender-radio-1']").click()
    page.get_by_placeholder('Mobile Number').fill('1234567891')
    data_birth_day.fill('24 Nov 1996')
    data_birth_day.press('Enter')
    subject.click()
    subject.press_sequentially('Arts')
    page.get_by_text('Arts', exact=True).click()
    page.locator("//*[@id='hobbies-checkbox-1']").click()
    page.get_by_placeholder('Current Address').fill('test')
    select_1.click()
    select_1.fill('ncr')
    select_1.press('Enter')
    select_2.click()
    select_2.fill('delhi')
    select_2.press('Enter')
    page.get_by_role('button', name='Submit').click()

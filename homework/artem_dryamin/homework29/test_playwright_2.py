from playwright.sync_api import Page, expect, BrowserContext


def test_1(page: Page):
    result = page.locator("//*[@id='result-text']")
    page.on('dialog', lambda allert: allert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    expect(result).to_have_text('Ok')


def test_2(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    link = page.get_by_role('link', name='Click')
    with context.expect_page() as new_page_event:
        link.click()
    page_2 = new_page_event.value
    result = page_2.locator("//*[@id='result-text']")
    expect(result).to_have_text('I am a new page in a new tab')
    expect(link).not_to_be_disabled()


def test_3(page: Page):
    button = page.locator("//*[@id='colorChange']")
    page.goto('https://demoqa.com/dynamic-properties')
    expect(button).to_have_attribute('class', 'mt-4 text-danger btn btn-primary', timeout=7000)
    button.click()

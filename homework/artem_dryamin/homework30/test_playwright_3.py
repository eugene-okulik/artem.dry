import json
from playwright.sync_api import Page, Route, expect


def test_change_response(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        iphone_17_pro = body['body']['digitalMat'][0]
        iphone_17_pro['productName'] = 'яблокофон 17 про'
        iphone_17_pro['familyTypes'][0]['productName'] = 'яблокофон 17 про'
        iphone_17_pro['familyTypes'][0]['tabTitle'] = 'яблокофон 17 про'
        route.fulfill(
            response=response,
            body=json.dumps(body),
        )

    page.route('**/digital-mat**', handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.get_by_role(
        'button',
        name='Take a closer look - iPhone 17 Pro & iPhone 17 Pro Max',
    ).click()
    title = page.locator('#rf-digitalmat-overlay-label-0').first
    expect(title).to_have_text('яблокофон 17 про')

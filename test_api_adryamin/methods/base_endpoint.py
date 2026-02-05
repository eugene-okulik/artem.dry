import allure


class Endpoint:
    url = f'http://objapi.course.qa-practice.com/object'
    headers = {'Content-type': 'application/json'}
    response = None
    json = None

    @allure.step('Check status code')
    def check_status_code(self, code):
        assert self.response.status_code == code

    @allure.step('Check name')
    def check_response_name(self, name):
        assert self.json['name'] == name

import allure
import requests
from methods.base_endpoint import Endpoint


class CreateObj(Endpoint):
    @allure.step('Create new obj')
    def create_new_obj(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=payload, headers=headers)
        self.json = self.response.json()
        return self.response


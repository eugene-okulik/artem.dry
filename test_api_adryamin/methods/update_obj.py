import allure
import requests
from methods.base_endpoint import Endpoint


class UpdateObj(Endpoint):
    @allure.step('Update obj')
    def update_new_obj(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/{post_id}', json=payload, headers=headers)
        self.json = self.response.json()
        return self.response

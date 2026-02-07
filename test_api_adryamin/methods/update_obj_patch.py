import requests
import allure
from methods.base_endpoint import Endpoint


class UpdateObjPatch(Endpoint):
    @allure.step('Update obj patch')
    def update_obj_patch(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(f'{self.url}/{post_id}', json=payload, headers=headers)
        self.json = self.response.json()
        return self.response

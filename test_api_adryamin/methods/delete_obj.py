import allure
import requests
from methods.base_endpoint import Endpoint


class DeleteObj(Endpoint):
    @allure.step('Delete obj')
    def delete_old_obj(self, post_id):
        self.response = requests.delete(f'{self.url}/{post_id}')

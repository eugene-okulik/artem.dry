from locust import task, HttpUser


data = {"name": "Artem_1", "data": {"Age": 29, "Proff": "New_AQA"}}
data2 = {"name": "Artem_2", "data": {"Age": 30, "Proffi": "New_AQAA"}}
data3 = {"name": "Artem_3"}
headers = {'Content-type': 'application/json'}


class MemeUser(HttpUser):

    @task
    def create_and_delete(self):
        response = self.client.post('/object', json=data, headers=headers)
        obj_id = response.json()['id']
        self.client.delete(f'/object/{obj_id}', headers=headers)

    @task
    def put_obj(self):
        self.client.put('/object/50', json=data2, headers=headers)

    @task
    def patch_obj(self):
        self.client.patch('/object/40', json=data3, headers=headers)

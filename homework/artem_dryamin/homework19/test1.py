import requests


def create_obj():
    data = {"name": "Artem",
            "data": {"Age": 29,
                     "Proff": "New_AQA"}
            }
    headers = {'Content-type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=data, headers=headers)
    assert response.json()['name'] == 'Artem'
    assert response.status_code


def new_obj():
    data = {"name": "Artem",
            "data": {"Age": 29,
                     "Proff": "New_AQA"}
            }
    headers = {'Content-type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=data, headers=headers).json()
    return response['id']


def update_obj():
    user_id = new_obj()
    data = {"name": "Artem_1",
            "data": {"Age": 29,
                     "Proff": "New_AQA"}
            }
    headers = {'Content-type': 'application/json'}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{user_id}', json=data, headers=headers)
    assert response.json()['name'] == 'Artem_1'
    assert response.status_code
    clear(user_id)


def update_obj_patch():
    user_id = new_obj()
    data = {"name": "Artem_22"}
    headers = {'Content-type': 'application/json'}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{user_id}', json=data, headers=headers)
    assert response.json()['name'] == 'Artem_22'
    assert response.status_code
    clear(user_id)


def clear(user_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{user_id}')


def delete_obj():
    user_id = new_obj()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{user_id}')
    assert response.status_code


create_obj()
update_obj()
update_obj_patch()
delete_obj()

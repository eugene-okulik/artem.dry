import requests
import pytest


@pytest.mark.critical
@pytest.mark.parametrize('name', ['Denis', 'Oleg', 'Petr'])
def test_create_obj(new_session, star_func, name):
    data = {"name": "Artem", "data": {"Age": 29, "Proff": "New_AQA"}}
    headers = {'Content-type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=data, headers=headers)
    assert response.json()['name'] == 'Artem'
    assert response.status_code == 200


@pytest.fixture(autouse=True)
def star_func():
    print("\nbefore test")
    yield
    print("after test")


@pytest.fixture(scope='session')
def new_session():
    print('Start testing')
    yield
    print('Testing completed')

@pytest.fixture()
def new_obj():
    data = {"name": "Artem", "data": {"Age": 29, "Proff": "New_AQA"}}
    headers = {'Content-type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=data, headers=headers).json()
    post_id = response['id']
    yield post_id
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')


@pytest.mark.medium
def test_update_obj(star_func, new_obj):
    data = {"name": "Artem_1",
            "data": {"Age": 29,
                     "Proff": "New_AQA"}
            }
    headers = {'Content-type': 'application/json'}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{new_obj}', json=data, headers=headers)
    assert response.json()['name'] == 'Artem_1'
    assert response.status_code == 200


def test_update_obj_patch(star_func, new_obj):
    data = {"name": "Artem_22"}
    headers = {'Content-type': 'application/json'}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{new_obj}', json=data, headers=headers)
    assert response.json()['name'] == 'Artem_22'
    assert response.status_code == 200



def test_delete_obj(star_func, new_obj):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_obj}')
    print(response.status_code)
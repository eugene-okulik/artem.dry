import pytest


new_data = [
    {"name": 'Artem1', "data": {"Age": 29, "Proff1": "New_AQA1"}},
    {"name": 'Artem2', "data": {"Age": 29, "Proff2": "New_AQA2"}},
    {"name": 'Artem3', "data": {"Age": 29, "Proff3": "New_AQA3"}}
]

data = {"name": "Artem_1", "data": {"Age": 29, "Proff": "New_AQA"}}

@pytest.mark.parametrize('data', new_data)
def test_create_obj(create_obj, data):
    create_obj.create_new_obj(data)
    create_obj.check_response_name(data['name'])
    create_obj.check_status_code(200)


def test_update_obj(post_id, update_obj):
    update_obj.update_new_obj(post_id, data)
    update_obj.check_status_code(200)
    update_obj.check_response_name(data['name'])


def test_delete_obj(delete_obj, post_id):
    delete_obj.delete_old_obj(post_id)
    delete_obj.check_status_code(200)
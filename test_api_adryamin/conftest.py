import pytest
from methods.create_obj import CreateObj
from methods.update_obj import UpdateObj
from methods.delete_obj import DeleteObj
from methods.update_obj_patch import UpdateObjPatch


@pytest.fixture()
def create_obj():
    return CreateObj()


@pytest.fixture()
def update_obj():
    return UpdateObj()


@pytest.fixture()
def delete_obj():
    return DeleteObj()


@pytest.fixture()
def update_obj_patch():
    return UpdateObjPatch()


@pytest.fixture()
def post_id(create_obj, delete_obj):
    data = {"name": "Artem", "data": {"Age": 29, "Proff": "test"}}
    create_obj.create_new_obj(data)
    post_id = create_obj.json['id']
    yield post_id
    delete_obj.delete_old_obj(post_id)

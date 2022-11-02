# -*- coding: utf-8 -*-
import json
import pytest
from fastapi.testclient import TestClient

from main import app
from tests.utils import UserSeed, Sqlite3
from tests.mocks.user import users

client = TestClient(app)


@pytest.fixture(autouse=True)
def run_around_tests():
    UserSeed.insert_all()
    yield
    UserSeed.remove_all()


def test_find_all_users_without_pagination():
    response = client.get("/users")
    assert len(response.json().get("users")) == 10


def test_find_all_users_with_limit_pagination():
    response = client.get("/users?limit=15")
    assert len(response.json().get("users")) == 15


def test_find_all_users_with_offset_pagination():
    response = client.get("/users?skip=8")
    assert len(response.json().get("users")) == len(users) - 8


def test_find_all_users_with_limit_and_offset_pagination():
    response = client.get("/users?skip=2&limit=15")
    assert len(response.json().get("users")) == len(users) - 2


def test_find_user_by_id():
    response = client.get("/users/111111111111111111111111")
    assert response.json().get("error") is None
    assert response.json().get("user") is not None


def test_should_return_error_when_not_find_user_by_id():
    response = client.get("/users/111111111111111111111112")
    error = response.json().get("detail")[0]
    assert "user_id" in error.get("loc")
    assert error.get("msg") == "User not found"
    assert response.status_code == 404


def test_create_user_with_valid_args():
    data = json.dumps(
        {"name": "string", "email": "string@gmail.com", "password": "string"}
    )
    response = client.post("/users", data)
    assert response.json().get("user") is not None


def test_create_user_with_missing_email():
    data = json.dumps({"name": "string", "password": "string"})
    response = client.post("/users", data)
    error = response.json().get("detail")[0]
    assert "email" in error.get("loc")
    assert error.get("type") == "value_error.missing"


def test_create_user_with_missing_password():
    data = json.dumps(
        {
            "name": "string",
            "email": "string@gmail.com",
        }
    )
    response = client.post("/users", data)
    error = response.json().get("detail")[0]
    assert "password" in error.get("loc")
    assert error.get("type") == "value_error.missing"


def test_create_user_with_missing_name():
    data = json.dumps({"email": "string@gmail.com", "password": "string"})
    response = client.post("/users", data)
    error = response.json().get("detail")[0]
    assert "name" in error.get("loc")
    assert error.get("type") == "value_error.missing"
    assert response.status_code == 422


def test_create_user_with_invalid_email():
    data = json.dumps({"name": "string", "email": "string", "password": "string"})
    response = client.post("/users", data)
    error = response.json().get("detail")[0]
    assert "email" in error.get("loc")
    assert error.get("type") == "value_error"


def test_inactivate_user_with_a_valid_userid():
    user = Sqlite3.find_by_id("111111111111111111111111")
    assert user.active == True

    response = client.post("/users/inactivate/111111111111111111111111")
    assert response.json().get("message") == "inactivated"

    user = Sqlite3.find_by_id("111111111111111111111111")
    assert user.active == False


def test_inactivate_user_with_an_invalid_userid():
    response = client.post("/users/inactivate/111111111111111111111112")
    error = response.json().get("detail")[0]
    assert "user_id" in error.get("loc")
    assert error.get("msg") == "User not found"
    assert response.status_code == 404

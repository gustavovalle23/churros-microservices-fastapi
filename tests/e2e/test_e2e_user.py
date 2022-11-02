# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient
import pytest

from main import app
from tests.seeds import UserSeed
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
    assert response.json().get("error") == "User Not Found"

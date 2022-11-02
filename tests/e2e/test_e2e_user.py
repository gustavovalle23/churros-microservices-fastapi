# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient
import pytest

from main import app
from tests.seeds import UserSeed

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
    assert len(response.json().get("users")) == 7


def test_find_all_users_with_limit_and_offset_pagination():
    response = client.get("/users?skip=2&limit=15")
    assert len(response.json().get("users")) == 13

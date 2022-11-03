# -*- coding: utf-8 -*-
import json
import pytest
from fastapi.testclient import TestClient

from main import app
from tests.utils import UserSeed

client = TestClient(app)


@pytest.fixture(autouse=True)
def run_around_tests():
    UserSeed.insert_all()
    yield
    UserSeed.remove_all()


def test_authenticate_user():
    data = {"username": "admin@gmail.com", "password": "admin"}
    response = client.post("/token", data)
    assert response.json().get("access_token") is not None
    assert response.json().get("token_type") == "bearer"

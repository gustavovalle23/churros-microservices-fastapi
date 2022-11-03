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
    print(response.json())

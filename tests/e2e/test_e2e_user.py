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


def test_find_user_by_id():
    response = client.get("/users")
    assert len(response.json().get("users")) == 2

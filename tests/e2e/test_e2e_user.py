# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_find_user_by_id():
    response = client.get("/users")
    assert response.json().get("users") == []

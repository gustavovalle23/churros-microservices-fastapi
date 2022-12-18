# -*- coding: utf-8 -*-
import pytest
from typing import Mapping
from fastapi.testclient import TestClient

from main import app
from src.bootstrap import bootstrap_di
from src.user.domain.__tests__.e2e.mocks.user import users
from src.user.domain.__tests__.e2e.utils import (
    UserSeed, Sqlite3, generate_token_user
)


bootstrap_di()
client = TestClient(app)


@pytest.fixture(autouse=True)
def run_around_tests():
    UserSeed.insert_all()
    yield
    UserSeed.remove_all()


endpoint = "/users"
token_endpoint = "/token"


class TestFindUser:

    def test_find_all_users_without_pagination(self):
        response = client.get(endpoint)
        assert len(response.json().get("users")) == 10

    def test_find_all_users_with_limit_pagination(self):
        response = client.get("/users?limit=15")
        assert len(response.json().get("users")) == 15

    def test_find_all_users_with_offset_pagination(self):
        response = client.get("/users?skip=8")
        assert len(response.json().get("users")) == len(users) - 8

    def test_find_all_users_with_limit_and_offset_pagination(self):
        response = client.get("/users?skip=2&limit=15")
        assert len(response.json().get("users")) == len(users) - 2

    def test_find_user_by_id(self):
        response = client.get("/users/1")
        assert response.json().get("error") is None
        assert response.json().get("user") is not None

    def test_should_return_error_when_not_find_user_by_id(self):
        response = client.get("/users/123")
        error = response.json().get("detail")[0]
        assert "user_id" in error.get("loc")
        assert error.get("msg") == "User not found"
        assert response.status_code == 404


email = "string@gmail.com"


class TestCreateUser:

    value_missing = "value_error.missing"

    def test_create_user_with_valid_args(self):
        data: Mapping[str, str] = {
            "name": "string", "email": email, "password": "string"}
        response = client.post(endpoint, json=data)
        assert response.json().get("user") is not None

    def test_create_user_with_missing_email(self):
        data: Mapping[str, str] = {"name": "string", "password": "string"}
        response = client.post(endpoint, json=data)
        error = response.json().get("detail")[0]
        assert "email" in error.get("loc")
        assert error.get("type") == self.value_missing

    def test_create_user_with_missing_password(self):
        data = {
            "name": "string",
            "email": email,
        }
        response = client.post(endpoint, json=data)
        error = response.json().get("detail")[0]
        assert "password" in error.get("loc")
        assert error.get("type") == self.value_missing

    def test_create_user_with_missing_name(self):
        data = {"email": email, "password": "string"}
        response = client.post(endpoint, json=data)
        error = response.json().get("detail")[0]
        assert "name" in error.get("loc")
        assert error.get("type") == self.value_missing
        assert response.status_code == 422

    def test_create_user_with_invalid_email(self):
        data = {"name": "string", "email": "string", "password": "string"}
        response = client.post(endpoint, json=data)
        error = response.json().get("detail")[0]
        assert "email" in error.get("loc")
        assert error.get("type") == "value_error"


class TestInactivateUser:

    def test_inactivate_user_with_a_valid_user(self):
        user = Sqlite3.find_by_id(1)
        assert user.active is True

        response = client.post(
            "/users/inactivate",
            headers={"Authorization": f"Bearer {generate_token_user(client)}"},
        )
        assert response.json().get("message") == "inactivated"

        user = Sqlite3.find_by_id(1)
        assert user.active is False


class TestUpdateUser:

    def test_update_user_with_valid_args(self):
        data = {
            "id": 1,
            "name": "name_updated",
            "email": email,
            "password": "string",
        }
        response = client.patch(endpoint, json=data)
        assert response.json().get("user", {}).get("name") == "name_updated"
        assert (
            response.json().get("user", {}).get("email") == email
        )

    def test_update_user_with_specific_fields(self):
        data = {
            "id": 1,
            "name": "name_updated",
        }
        response = client.patch(endpoint, json=data)
        assert response.json().get("user", {}).get("name") == "name_updated"
        assert response.json().get("user", {}).get("email") == "admin1@gmail.com"

    def test_update_user_with_invalid_userid(self):
        data = {
            "id": "112",
            "name": "name_updated",
            "email": "string_updated@gmail.com",
            "password": "string",
        }
        response = client.patch(endpoint, json=data)
        error = response.json().get("detail")[0]
        assert "user_id" in error.get("loc")
        assert error.get("msg") == "User not found"
        assert response.status_code == 404

    def test_update_user_with_invalid_email(self):
        data = {
            "id": 1,
            "name": "name_updated",
            "email": "admin@sqs",
            "password": "string",
        }
        response = client.patch(endpoint, json=data)
        error = response.json().get("detail")[0]
        assert "email" in error.get("loc")
        assert error.get("type") == "value_error"

    def test_update_user_with_already_registered_email(self):
        data = {
            "id": 1,
            "name": "name_updated",
            "email": "admin2@gmail.com",
            "password": "string",
        }
        response = client.patch(endpoint, json=data)
        error = response.json().get("detail")[0]
        assert "email" in error.get("loc")
        assert error.get("msg") == "Email already registered"
        assert error.get("type") == "already_registered_error"


class TestDeleteUser:

    def test_delete_user_with_a_valid_user(self):
        response = client.delete(
            endpoint, headers={
                "Authorization": f"Bearer {generate_token_user(client)}"}
        )
        assert response.json().get("message") == "deleted"

        user = Sqlite3.find_by_id(1)
        original_user = list(
            filter(lambda user: user.get("id") == 1, users))[0]
        assert user.name != original_user.get("name")
        assert user.email != original_user.get("email")
        assert user.password != original_user.get("password")
        assert not original_user.get("password").startswith("deleted")
        assert user.password.startswith("deleted")
        assert user.active is False


class TestAuthUser:

    def test_authenticate_user_with_correct_credentials(self):
        data = {"username": "admin1@gmail.com", "password": "admin"}
        response = client.post(token_endpoint, data=data)
        assert response.json().get("access_token") is not None
        assert response.json().get("token_type") == "bearer"

    def test_authenticate_user_with_incorrect_password(self):
        data = {"username": "admin@gmail.com", "password": "admin2"}
        response = client.post(token_endpoint, data=data)
        assert response.status_code == 401
        assert response.json().get("detail") is not None
        assert response.json().get("detail") == "Incorrect username or password"

    def test_authenticate_user_with_incorrect_email(self):
        data = {"username": "incorrect@gmail.com", "password": "admin"}
        response = client.post(token_endpoint, data=data)
        assert response.status_code == 401
        assert response.json().get("detail") is not None
        assert response.json().get("detail") == "Incorrect username or password"

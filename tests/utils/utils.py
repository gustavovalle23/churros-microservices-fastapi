# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from tests.utils.mocks.user import users
from app.core.database.models import UserModel, engine


class UserSeed:
    @staticmethod
    def insert_all():
        with Session(engine) as session:
            models = [UserModel(**user) for user in users]
            session.add_all(models)
            session.commit()

    @staticmethod
    def remove_all():
        with Session(engine) as session:
            session.query(UserModel).delete()
            session.commit()


class Sqlite3:
    @staticmethod
    def find_by_id(user_id: int):
        with Session(engine) as session:
            return session.query(UserModel).filter_by(id=user_id).first()


def generate_token_user(client: TestClient) -> str:
    data = {"username": "admin1@gmail.com", "password": "admin"}
    response = client.post("/token", data=data).json()
    return response.get("access_token")

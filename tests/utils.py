# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from tests.mocks.user import users
from src.infra.database import UserModel, engine


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
    def find_by_id(user_id: str):
        with Session(engine) as session:
            return session.query(UserModel).filter_by(id=user_id).first()


def generate_token_user(client: TestClient) -> str:
    data = {"username": "admin@gmail.com", "password": "admin"}
    return client.post("/token", data).json().get("access_token")

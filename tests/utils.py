# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session

from src.infra.database import UserModel, engine
from tests.mocks.user import users


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

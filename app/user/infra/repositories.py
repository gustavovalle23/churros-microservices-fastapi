# -*- coding: utf-8 -*-
import bcrypt
import random
import string
import orjson as json
from typing import Tuple
from sqlalchemy.sql.expression import true

from app.user.domain.entities import User
from app.user.domain.factories import UserFactory
from app.core.database.models import UserModel, db_session
from app.api.routers.dtos.user import CreateUserInput, UpdateUserInput


class UserSqlachemyRepository:
    def find_all(self, skip: int = 0, limit: int = 100) -> Tuple[User]:

        db = db_session.get()

        users = (
            db.query(UserModel)
            .filter(UserModel.active == true())
            .offset(skip)
            .limit(limit)
        )
        return tuple(map(UserFactory.create, users))

    def find_by_email(self, email: str) -> User | None:
        db = db_session.get()

        user = db.query(UserModel).filter(UserModel.email == email).first()
        if not user:
            return

        return UserFactory.create(user)

    def find_by_id(self, user_id: int) -> User | None:
        db = db_session.get()

        user = (
            db.query(UserModel)
            .filter(UserModel.id == user_id)
            .filter(UserModel.active == true())
            .first()
        )
        if not user:
            return

        return UserFactory.create(user)

    def save(self, input: CreateUserInput) -> User:
        db = db_session.get()

        input.password = bcrypt.hashpw(input.password.encode(), bcrypt.gensalt())

        user = UserModel(**json.loads(input.json()))
        db.add(user)
        db.commit()

        return UserFactory.create(user)

    def update(self, update_user_input: UpdateUserInput) -> User:
        db = db_session.get()

        user_id = update_user_input.id
        data: dict = json.loads(update_user_input.json())
        data = {k: v for k, v in data.items() if v is not None and k != "id"}

        db.query(UserModel).filter(UserModel.id == user_id).update(data)
        db.commit()

        updated_user = (
            db.query(UserModel).filter(UserModel.id == update_user_input.id).first()
        )
        return UserFactory.create(updated_user)

    def inactivate(self, user_id: int) -> None:
        db = db_session.get()
        db.query(UserModel).filter(UserModel.id == user_id).update({"active": False})
        db.commit()

    def delete(self, user_id: int) -> None:
        db = db_session.get()

        db.query(UserModel).filter(UserModel.id == user_id).update(
            {
                "email": self.random_string(),
                "active": False,
                "name": self.random_string(),
                "password": f"deleted_{self.random_string(50)}",
            }
        )
        db.commit()

    @staticmethod
    def random_string(size=10):
        return "".join(
            random.choice(string.ascii_lowercase + string.digits) for _ in range(size)
        )

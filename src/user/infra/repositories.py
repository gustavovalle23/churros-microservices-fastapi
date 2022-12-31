# -*- coding: utf-8 -*-
import json
import bcrypt
import random
import string
from typing import Tuple
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import true

from src.user.domain.entities import User
from src.user.domain.factories import UserFactory
from src.infra.database import UserModel
from src.api.routers.dtos.user import CreateUserInput, UpdateUserInput


class UserSqlachemyRepository:
    def find_all(self, db: Session, skip: int = 0, limit: int = 100) -> Tuple[User]:

        users = (
            db.query(UserModel)
            .filter(UserModel.active == true())
            .offset(skip)
            .limit(limit)
        )
        return tuple(map(UserFactory.create, users))

    def find_by_email(self, db: Session, email: str) -> User | None:
        user = db.query(UserModel).filter(UserModel.email == email).first()
        if not user:
            return
        return UserFactory.create(user)

    def find_by_id(self, db: Session, user_id: int) -> User | None:
        user = (
            db.query(UserModel)
            .filter(UserModel.id == user_id)
            .filter(UserModel.active == true())
            .first()
        )
        if not user:
            return

        return UserFactory.create(user)

    def save(self, db: Session, input: CreateUserInput) -> User:
        input.password = bcrypt.hashpw(input.password.encode(), bcrypt.gensalt())
        user = UserModel(**json.loads(input.json()))
        db.add(user)
        db.commit()

        return UserFactory.create(user)

    def update(self, db: Session, update_user_input: UpdateUserInput) -> User:
        user_id = update_user_input.id
        data: dict = json.loads(update_user_input.json())
        data = {k: v for k, v in data.items() if v is not None and k != "id"}

        db.query(UserModel).filter(UserModel.id == user_id).update(data)
        db.commit()

        updated_user = (
            db.query(UserModel).filter(UserModel.id == update_user_input.id).first()
        )
        return UserFactory.create(updated_user)

    def inactivate(self, db: Session, user_id: int) -> None:
        db.query(UserModel).filter(UserModel.id == user_id).update({"active": False})
        db.commit()

    def delete(self, db: Session, user_id: int) -> None:
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

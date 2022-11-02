# -*- coding: utf-8 -*-
import random
import string
from uuid import uuid1 as uuid
from sqlalchemy.orm import Session, Query

from src.domain.user import User
from src.infra.database import UserModel
from src.application.dtos.user import CreateUserInput, UpdateUserInput


def to_entity(model: Query | UserModel) -> User | None:
    if not model:
        return

    return User(
        model.id,
        model.name,
        model.email,
        model.password,
        model.active,
        model.created_at,
        model.updated_at,
    )


def find_all(db: Session, skip: int = 0, limit: int = 100):
    users = (
        db.query(UserModel).filter(UserModel.active == True).offset(skip).limit(limit)
    )
    return tuple(map(to_entity, users))


def find_by_email(db: Session, email: str) -> User | None:
    user = db.query(UserModel).filter(UserModel.email == email).first()
    return to_entity(user)


def find_by_id(db: Session, user_id: str) -> User | None:
    user = (
        db.query(UserModel)
        .filter(UserModel.id == user_id)
        .filter(UserModel.active == True)
        .first()
    )
    return to_entity(user)


def save(db: Session, input: CreateUserInput) -> User:
    user = UserModel(
        id=uuid().hex, name=input.name, email=input.email, password=input.password
    )
    db.add(user)
    db.commit()
    return to_entity(user)


def update(db: Session, input: UpdateUserInput) -> User:
    db.query(UserModel).filter(UserModel.id == input.id).update(
        {"email": input.email, "name": input.name}
    )
    db.commit()
    updated_user = db.query(UserModel).filter(UserModel.id == input.id).first()
    return to_entity(updated_user)


def inactivate(db: Session, user_id: str) -> None:
    db.query(UserModel).filter(UserModel.id == user_id).update({"active": False})
    db.commit()


def delete(db: Session, user_id: str) -> None:
    db.query(UserModel).filter(UserModel.id == user_id).update(
        {"email": random_string(), "active": False, "password": random_string()}
    )
    db.commit()


def random_string():
    return "".join(
        random.choice(string.ascii_lowercase + string.digits) for _ in range(10)
    )

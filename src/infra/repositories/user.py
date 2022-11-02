# -*- coding: utf-8 -*-
import random
import string
from typing import Optional
from datetime import datetime
from uuid import UUID as uuid
from sqlalchemy.orm import Session

from domain.user import User
from infra.database import UserModel
from application.dtos.user import CreateUserInput, UpdateUserInput


def find_all(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(UserModel).filter(UserModel.active == True).offset(skip).limit(limit)
    )


def find_by_email(db: Session, email: str) -> User | None:
    user: Optional[UserModel] = db.query(UserModel).where(UserModel.email == email)
    return user


def find_by_id(db: Session, user_id: int) -> User | None:
    user = (
        db.query(UserModel)
        .filter(UserModel.id == user_id)
        .filter(UserModel.active == True)
        .first()
    )
    return user


def save(db: Session, input: CreateUserInput):
    user = UserModel(
        id=uuid(), name=input.name, email=input.email, password=input.password
    )
    db.add(user)
    db.commit()
    return user


def update(db: Session, user_id: int, input: UpdateUserInput) -> None:
    db.query(UserModel).filter(UserModel.id == user_id).update(
        {"email": input.email, "active": input.active}
    )
    db.commit()


def inactivate(db: Session, user_id: int) -> None:
    db.query(UserModel).filter(UserModel.id == user_id).update({"active": False})
    db.commit()


def delete(db: Session, user_id: int) -> None:
    db.query(UserModel).filter(UserModel.id == user_id).update(
        {"email": random_string(), "active": False, "password": random_string()}
    )
    db.commit()


def random_string():
    return "".join(
        random.choice(string.ascii_lowercase + string.digits) for _ in range(10)
    )

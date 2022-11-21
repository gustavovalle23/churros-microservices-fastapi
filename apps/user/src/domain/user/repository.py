# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session
from abc import ABC
from typing import List

from src.domain.user.entity import User


class UserRepository(ABC):
    def find_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        pass

    def to_entity(self, model) -> User | None:
        pass

    def find_all(self, db: Session, skip: int = 0, limit: int = 100):
        pass

    def find_by_email(self, db: Session, email: str) -> User | None:
        pass

    def find_by_id(self, db: Session, user_id: str) -> User | None:
        pass

    def save(self, db: Session, input) -> User:
        pass

    def update(self, db: Session, input) -> User:
        pass

    def inactivate(self, db: Session, user_id: str) -> None:
        pass

    def delete(self, db: Session, user_id: str) -> None:
        pass

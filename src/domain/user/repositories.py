# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session
from abc import ABC
from typing import Tuple

from src.domain.user.entities import User


class UserRepository(ABC):
    def find_all(self, db: Session, skip: int = 0, limit: int = 100) -> Tuple[User]:
        """
        Method responsable for find all users considering pagination
        """
        pass

    def find_by_email(self, db: Session, email: str) -> User | None:
        """
        Method responsable for find user by email
        """
        pass

    def find_by_id(self, db: Session, user_id: int) -> User | None:
        """
        Method responsable for find user by email
        """
        pass

    def save(self, db: Session, input_repository) -> User:
        """
        Method responsable for save user
        """
        pass

    def update(self, db: Session, input_repository) -> User:
        """
        Method responsable for update user
        """
        pass

    def inactivate(self, db: Session, user_id: int) -> None:
        """
        Method responsable for inactive user
        """
        pass

    def delete(self, db: Session, user_id: int) -> None:
        """
        Method responsable for delete user
        """
        pass

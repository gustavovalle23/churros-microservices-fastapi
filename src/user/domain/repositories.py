# -*- coding: utf-8 -*-
from abc import ABC
from typing import Tuple

from src.user.domain.entities import User


class UserRepository(ABC):
    def find_all(self, skip: int = 0, limit: int = 100) -> Tuple[User]:
        """
        Method responsable for find all users considering pagination
        """
        pass

    def find_by_email(self, email: str) -> User | None:
        """
        Method responsable for find user by email
        """
        pass

    def find_by_id(self, user_id: int) -> User | None:
        """
        Method responsable for find user by email
        """
        pass

    def save(self, input_repository) -> User:
        """
        Method responsable for save user
        """
        pass

    def update(self, input_repository) -> User:
        """
        Method responsable for update user
        """
        pass

    def inactivate(self, user_id: int) -> None:
        """
        Method responsable for inactive user
        """
        pass

    def delete(self, user_id: int) -> None:
        """
        Method responsable for delete user
        """
        pass

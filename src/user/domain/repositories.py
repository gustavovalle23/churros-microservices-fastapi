# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import Tuple, Any

from src.user.domain.entities import User


class UserRepository(ABC):
    @abstractmethod
    def find_all(self, skip: int = 0, limit: int = 100) -> Tuple[User]:
        """
        Method responsable for find all users considering pagination
        """
        pass

    @abstractmethod
    def find_by_email(self, db: Any, email: str) -> User | None:
        """
        Method responsable for find user by email
        """
        pass

    @abstractmethod
    def find_by_id(self, db: Any, user_id: int) -> User | None:
        """
        Method responsable for find user by email
        """
        pass

    @abstractmethod
    def save(self, input_repository) -> User:
        """
        Method responsable for save user
        """
        pass

    @abstractmethod
    def update(self, input_repository) -> User:
        """
        Method responsable for update user
        """
        pass

    @abstractmethod
    def inactivate(self, user_id: int) -> None:
        """
        Method responsable for inactive user
        """
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        """
        Method responsable for delete user
        """
        pass

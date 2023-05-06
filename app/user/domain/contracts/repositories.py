# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import Tuple, Any

from app.user.domain.entities import User


class UserRepository(ABC):
    @abstractmethod
    def find_all(self, skip: int = 0, limit: int = 100) -> Tuple[User]:
        """
        Method responsable for find all users considering pagination
        """
        raise NotImplementedError()

    @abstractmethod
    def find_by_email(self, email: str) -> User | None:
        """
        Method responsable for find user by email
        """
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self, user_id: int) -> User | None:
        """
        Method responsable for find user by email
        """
        raise NotImplementedError()

    @abstractmethod
    def save(self, input_repository) -> User:
        """
        Method responsable for save user
        """
        raise NotImplementedError()

    @abstractmethod
    def update(self, input_repository) -> User:
        """
        Method responsable for update user
        """
        raise NotImplementedError()

    @abstractmethod
    def inactivate(self, user_id: int) -> None:
        """
        Method responsable for inactive user
        """
        raise NotImplementedError()

    @abstractmethod
    def delete(self, user_id: int) -> None:
        """
        Method responsable for delete user
        """
        raise NotImplementedError()

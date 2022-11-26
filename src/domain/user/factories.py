from typing import Any

from src.domain.user.validators import UserValidator
from src.domain.user.entity import User


class UserValidatorFactory:
    @staticmethod
    def create():
        return UserValidator()


class UserFactory:

    @staticmethod
    def create(user: Any) -> User:

        return User(
            user.id,
            user.name,
            user.email,
            user.password,
            user.active,
            user.created_at,
            user.updated_at,
        )
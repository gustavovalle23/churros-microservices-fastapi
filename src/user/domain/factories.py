from typing import Any

from src.user.domain.validators import UserValidator
from src.user.domain.entities import create_user, User


class UserValidatorFactory:
    @staticmethod
    def create():
        return UserValidator()


class UserFactory:
    from src.core.database.models import UserModel
    @staticmethod
    def create(user: UserModel) -> User:
        return create_user(
            user.name,
            user.email,
            user.password,
            active=user.active,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

        # return User(
        #     user.id,
        #     user.name,
        #     user.email,
        #     user.password,
        #     user.active,
        #     user.created_at,
        #     user.updated_at,
        # )

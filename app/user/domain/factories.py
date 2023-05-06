from app.user.domain.validators import UserValidator
from app.user.domain.entities import User


class UserValidatorFactory:
    @staticmethod
    def create():
        return UserValidator()


class UserFactory:
    from app.core.database.models import UserModel
    @staticmethod
    def create(user: UserModel) -> User:
        return User(
            user.id,
            user.name,
            user.email,
            user.password,
            user.active,
            user.created_at,
            user.updated_at,
        )

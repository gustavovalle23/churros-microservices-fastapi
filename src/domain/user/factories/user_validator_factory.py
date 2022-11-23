from src.domain.user.validators import UserValidator

class UserValidatorFactory:
    @staticmethod
    def create():
        return UserValidator()

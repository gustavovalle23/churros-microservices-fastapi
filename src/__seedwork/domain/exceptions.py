from src.__seedwork.domain.validators import ErrorFields


class EntityValidationException(Exception):
    error: ErrorFields

    def __init__(self, error: ErrorFields) -> None:
        self.error = error
        super().__init__("Entity Validation Error")


class ValidationException(Exception):
    pass


class NotFoundException(Exception):
    pass

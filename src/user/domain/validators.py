# -*- coding: utf-8 -*-
import re
from typing import List

from src.user.domain.entities import User

regex_email = re.compile(
    r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
)


class UserValidator:
    errors: List[str] = []

    def validate(self, user: User) -> None:
        errors: List[str] = []

        if not user.name:
            errors.append("User: name is required!")

        if not user.email or not bool(re.fullmatch(regex_email, user.email)):
            errors.append("User: Should be a valid e-mail!")

        self.errors = errors

    def has_errors(self) -> bool:
        return bool(self.errors)

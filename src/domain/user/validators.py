# -*- coding: utf-8 -*-
from typing import Dict, List


class UserValidator:

    errors: Dict[str, List[str]] = []

    def validate(self, user: dict) -> bool:
        if len(user.email) == 0:
            self.errors.append("Should be a valid e-mail!")

        return len(self.errors) == 0


class UserValidatorFactory:
    @staticmethod
    def create():
        return UserValidator()

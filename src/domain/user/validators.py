# -*- coding: utf-8 -*-
import re
from typing import Dict, List

class UserValidator:
    errors: Dict[str, List[str]] = []

    def validate(self, user) -> bool:
        errors = []
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if not bool(re.fullmatch(regex, user.email)):
            errors.append(f"email: Should be a valid e-mail!")

        self.errors = errors if errors else []

        return len(self.errors) == 0

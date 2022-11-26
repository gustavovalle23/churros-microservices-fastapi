# -*- coding: utf-8 -*-
from typing import Optional
from datetime import datetime
from dataclasses import dataclass

from src.__shared.entity import Entity


@dataclass(slots=True, frozen=True)
class User(Entity):
    id: str
    name: str
    email: str
    password: str
    active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def activate(self):
        self.__setattr__('active', True)

    def __post_init__(self):
        self.validate()

    def validate(self):
        from src.domain.user.factories import UserValidatorFactory

        validator = UserValidatorFactory.create()
        is_valid = validator.validate(self)

        if not is_valid:
            raise ValueError(validator.errors)

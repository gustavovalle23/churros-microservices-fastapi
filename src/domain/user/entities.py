# -*- coding: utf-8 -*-
from typing import Optional
from datetime import datetime
from dataclasses import dataclass

from src.__shared.domain.entities import Entity
from src.domain.user.value_objects import Address


@dataclass(frozen=True)
class User(Entity):
    id: int
    name: str
    email: str
    password: str
    active: bool
    points: int = 0
    address: Address = None
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = None

    def activate(self):
        self.__setattr__('active', True)

    def __post_init__(self):
        self.validate()

    def increase_points(self, points: int):
        self.points += points

    def validate(self):
        from src.domain.user.factories import UserValidatorFactory

        validator = UserValidatorFactory.create()
        is_valid = validator.validate(self)

        if not is_valid:
            raise ValueError(validator.errors)

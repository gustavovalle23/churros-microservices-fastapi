# -*- coding: utf-8 -*-
from typing import Optional
from datetime import datetime
from dataclasses import dataclass

from src.__seedwork.domain.entities import Entity
from src.user.domain.value_objects import Address


@dataclass(frozen=True)
class User(Entity):
    name: str
    email: str
    password: str
    active: bool
    points: int = 0
    address: Optional[Address] = None
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None

    def activate(self):
        self.__setattr__("active", True)

    def __post_init__(self):
        self.validate()

    def increase_points(self, points: int):
        self.__setattr__("points", self.points + points)

    def validate(self):
        from src.user.domain.factories import UserValidatorFactory

        validator = UserValidatorFactory.create()
        is_valid = validator.validate(self)

        if not is_valid:
            raise ValueError(validator.errors)

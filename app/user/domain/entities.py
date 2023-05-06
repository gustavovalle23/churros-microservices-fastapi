# -*- coding: utf-8 -*-
from typing import Optional
from datetime import datetime
from dataclasses import dataclass

from app.__seedwork.domain.entities import Entity
from app.user.domain.value_objects import Address
from app.user.domain.errors import NotificationError


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

    def __post_init__(self):
        self.validate()

    def activate(self):
        self.__setattr__("active", True)

    def increase_points(self, points: int):
        self.__setattr__("points", self.points + points)

    def validate(self):
        from app.user.domain.factories import UserValidatorFactory

        validator = UserValidatorFactory.create()
        validator.validate(self)

        if validator.has_errors():
            raise NotificationError(validator.errors)

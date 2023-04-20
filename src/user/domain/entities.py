# -*- coding: utf-8 -*-
from typing import Optional
from datetime import datetime
from dataclasses import dataclass
from collections import namedtuple

from src.__seedwork.domain.entities import Entity
from src.user.domain.value_objects import Address
from src.user.domain.errors import NotificationError


# @dataclass(frozen=True)
# class User(Entity):
#     name: str
#     email: str
#     password: str
#     active: bool
#     points: int = 0
#     address: Optional[Address] = None
#     created_at: datetime = datetime.now()
#     updated_at: Optional[datetime] = None

#     def __post_init__(self):
#         self.validate()

#     def activate(self):
#         self.__setattr__("active", True)

#     def increase_points(self, points: int):
#         self.__setattr__("points", self.points + points)

#     def validate(self):
#         from src.user.domain.factories import UserValidatorFactory

#         validator = UserValidatorFactory.create()
#         validator.validate(self)

#         if validator.has_errors():
#             raise NotificationError(validator.errors)


User = namedtuple('User', ['name', 'email', 'password', 'active', 'points', 'address', 'created_at', 'updated_at'])

def create_user(name: str, email: str, password: str, active: bool, points: int = 0,
                address: Optional[Address] = None, created_at: datetime = datetime.now(),
                updated_at: Optional[datetime] = None) -> User:

    from src.user.domain.factories import UserValidatorFactory
    
    user = User(name, email, password, active, points, address, created_at, updated_at)

    validator = UserValidatorFactory.create()
    validator.validate(user)

    if validator.has_errors():
        raise NotificationError(validator.errors)


    user.activate = lambda: user._replace(active=True)
    user.increase_points = lambda points: user._replace(points=user.points + points)

    return user

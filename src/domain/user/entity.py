# -*- coding: utf-8 -*-
from datetime import datetime
from dataclasses import dataclass

from src.__shared.entity import Entity
from src.domain.user.factories.user_validator_factory import UserValidatorFactory


@dataclass(frozen=True, slots=True)
class User(Entity):
    id: str
    name: str
    email: str
    password: str
    active: bool
    created_at: datetime = None
    updated_at: datetime = None

    def activate(self):
        self.activate = True

    def __post_init__(self):
        self.validate()

    def validate(self):
        validator = UserValidatorFactory.create()

        is_valid = validator.validate(self)

        if not is_valid:
            raise ValueError(validator.errors)

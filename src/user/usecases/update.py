# -*- coding: utf-8 -*-
from typing import Optional
from dataclasses import dataclass

from src.user.domain.entities import User
from src.user.domain.repositories import UserRepository
from src.__seedwork.application.use_cases import UseCase
from src.api.routers.errors import (
    UserNotFound,
    EmailAlreadyRegistered,
)


@dataclass(slots=True, frozen=True)
class Input:
    id: int
    name: str
    email: str


@dataclass(slots=True, frozen=True)
class Output:
    id: int
    name: str
    email: str
    active: bool


@dataclass(slots=True, frozen=True)
class UpdateUserUseCase(UseCase):

    user_repository: UserRepository

    def execute(self, input: Input) -> Output:
        user: Optional[User] = self.user_repository.find_by_id(input.id)
        if not user:
            raise UserNotFound._raise()

        if self.user_repository.find_by_email(input.email):
            raise EmailAlreadyRegistered._raise()

        updated_user = self.user_repository.update(input)

        return Output(
            updated_user.id, updated_user.name, updated_user.email, updated_user.active
        )

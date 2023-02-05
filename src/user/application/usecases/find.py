# -*- coding: utf-8 -*-
from typing import Optional
from dataclasses import dataclass

from src.user.domain.entities import User
from src.user.domain.repositories import UserRepository
from src.__seedwork.application.use_cases import UseCase
from src.api.routers.errors import (
    UserNotFound,
)


@dataclass(slots=True, frozen=True)
class Input:
    id: int


@dataclass(slots=True, frozen=True)
class Output:
    name: str
    email: str
    active: bool


@dataclass(slots=True, frozen=True)
class FindUserUseCase(UseCase):

    user_repository: UserRepository

    def execute(self, input: Input) -> Output:
        user: Optional[User] = self.user_repository.find_by_id(input.id)

        if not user:
            return UserNotFound()

        return Output(user.name, user.email, user.active)

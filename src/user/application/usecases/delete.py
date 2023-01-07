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
class DeleteUserUseCase(UseCase):

    user_repository: UserRepository

    def execute(self, input: Input) -> None:
        user: Optional[User] = self.user_repository.find_by_id(input.id)
        if not user:
            return UserNotFound()

        self.user_repository.delete(input.id)

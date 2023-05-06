# -*- coding: utf-8 -*-
from typing import Optional
from dataclasses import dataclass

from app.user.domain.entities import User
from app.user.domain.contracts.repositories import UserRepository
from app.__seedwork.application.use_cases import UseCase
from app.api.routers.errors import (
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
            raise UserNotFound._raise()

        self.user_repository.delete(input.id)

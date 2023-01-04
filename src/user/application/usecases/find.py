# -*- coding: utf-8 -*-
from dataclasses import dataclass
from sqlalchemy.orm import Session
from typing import Optional

from src.user.domain.repositories import UserRepository
from src.__seedwork.application.use_cases import UseCase
from src.api.routers.errors import (
    UserNotFound,
)


@dataclass(slots=True, frozen=True)
class Input:
    email: Optional[str]
    id: Optional[int]


@dataclass(slots=True, frozen=True)
class Output:
    name: str
    email: str
    active: bool


@dataclass(slots=True, frozen=True)
class FindUserUseCase(UseCase):

    user_repository: UserRepository

    def execute(self, input: Input, db: Session) -> Output:
        if input.id:
            user = self.user_repository.find_by_id(db, input.id)
        else:
            user = self.user_repository.find_by_email(db, input.email)

        if not user:
            return UserNotFound()

        return Output(user.name, user.email, user.active)

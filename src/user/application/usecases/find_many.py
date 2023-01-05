# -*- coding: utf-8 -*-
from typing import Tuple
from dataclasses import dataclass
from sqlalchemy.orm import Session

from src.user.domain.repositories import UserRepository
from src.__seedwork.application.use_cases import UseCase


@dataclass(slots=True, frozen=True)
class Input:
    skip: int
    limit: int


@dataclass(slots=True, frozen=True)
class FindUsersOutput:
    name: str
    email: str
    active: bool


@dataclass(slots=True, frozen=True)
class Output:
    users: Tuple[FindUsersOutput]


@dataclass(slots=True, frozen=True)
class FindUsersUseCase(UseCase):

    user_repository: UserRepository

    def execute(self, input: Input, db: Session) -> Output:
        users = self.user_repository.find_all(db, input.skip, input.limit)
        outputs = [
            FindUsersOutput(user.name, user.email, user.activate) for user in users
        ]
        return Output(outputs)

# -*- coding: utf-8 -*-
from typing import Tuple, Optional
from dataclasses import dataclass

from app.user.domain.contracts.repositories import UserRepository
from app.__seedwork.application.use_cases import UseCase


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
    input: Optional[Input] = None

    def prepare_input(self, skip: int, limit: int) -> 'FindUsersUseCase':
        object.__setattr__(self, "input", Input(skip, limit))
        return self

    def execute(self) -> Output:
        users = self.user_repository.find_all(self.input.skip, self.input.limit)
        outputs = [
            FindUsersOutput(user.name, user.email, user.activate) for user in users
        ]
        return Output(outputs)

# -*- coding: utf-8 -*-
from dataclasses import dataclass

from src.user.domain.entities import User
from src.user.domain.repositories import UserRepository
from src.__seedwork.application.use_cases import UseCase
from src.user.domain.errors import EmailAlreadyRegisteredError


@dataclass(slots=True, frozen=True)
class Input:
    name: str
    email: str
    password: str
    active: bool = True


@dataclass(slots=True, frozen=True)
class Output:
    name: str
    email: str
    active: bool = True


@dataclass(slots=True, frozen=True)
class CreateUserUseCase(UseCase):

    user_repository: UserRepository

    def execute(self, input_use_case: Input) -> Output:
        if self.user_repository.find_by_email(input_use_case.email):
            raise EmailAlreadyRegisteredError(input_use_case.email)

        user_created: User = self.user_repository.save(input_use_case)
        return Output(user_created.name, user_created.email, user_created.active)

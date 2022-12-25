# -*- coding: utf-8 -*-
import bcrypt
from dataclasses import dataclass
from sqlalchemy.orm import Session

from src.__seedwork.application.use_cases import UseCase
from src.user.domain.repositories import UserRepository


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

    def execute(self, input_use_case: Input, db: Session) -> Output:
        input_use_case.__setattr__(
            "password",
            bcrypt.hashpw(input_use_case.password.encode(), bcrypt.gensalt()),
        )

        user_created = self.user_repository.save(db, input_use_case)
        return Output(user_created.name, user_created.email, user_created.active)

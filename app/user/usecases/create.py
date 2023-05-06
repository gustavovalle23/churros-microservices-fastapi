# -*- coding: utf-8 -*-
from dataclasses import dataclass

from app.user.domain.entities import User
from app.user.domain.contracts.repositories import UserRepository
from app.user.domain.contracts.gateways import SyncCloud
from app.__seedwork.application.use_cases import UseCase
from app.user.domain.errors import EmailAlreadyRegisteredError


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
    sync_cloud: SyncCloud

    def execute(self, input_use_case: Input) -> Output:
        if self.user_repository.find_by_email(input_use_case.email):
            raise EmailAlreadyRegisteredError(input_use_case.email)

        user_created: User = self.user_repository.save(input_use_case)
        self.sync_cloud.send_user(user_created)

        return Output(user_created.name, user_created.email, user_created.active)

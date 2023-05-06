# -*- coding: utf-8 -*-
from datetime import timedelta
from dataclasses import dataclass


from app.api.routers.errors import (
    IncorrectUsernameOrPassword,
)
from app.user.domain.contracts.repositories import UserRepository
from app.__seedwork.application.use_cases import UseCase
from app.user.infra.gateways.jwt import (
    authenticate_user,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)


@dataclass(slots=True, frozen=True)
class Input:
    username: str
    password: str


@dataclass(slots=True, frozen=True)
class Output:
    access_token: str


@dataclass(slots=True, frozen=True)
class LoginUserUseCase(UseCase):

    user_repository: UserRepository

    def execute(self, input: Input) -> Output:
        user = authenticate_user(input.username, input.password)
        if not user:
            return IncorrectUsernameOrPassword()

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )

        return Output(access_token)

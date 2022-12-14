# -*- coding: utf-8 -*-
from kink import di

from src.domain.user.repositories import UserRepository

from src.infra.user.repositories.user import UserSqlachemyRepository


def bootstrap_di() -> None:
    di[UserRepository] = UserSqlachemyRepository()

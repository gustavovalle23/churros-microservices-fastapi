# -*- coding: utf-8 -*-
from kink import di

from src.user.domain.repositories import UserRepository
from src.infra.user.repositories.user import UserSqlachemyRepository


def bootstrap_di() -> None:
    di[UserRepository] = UserSqlachemyRepository()

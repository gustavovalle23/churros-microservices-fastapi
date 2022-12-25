# -*- coding: utf-8 -*-
from kink import di

from src.user.domain.repositories import UserRepository
from src.user.infra.repositories import UserSqlachemyRepository


def bootstrap_di() -> None:
    di[UserRepository] = UserSqlachemyRepository()

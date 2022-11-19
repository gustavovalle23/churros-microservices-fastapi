# -*- coding: utf-8 -*-
from kink import di

from src.user.domain.contracts.repository import UserRepository

from src.user.infra.repositories.user import UserSqlachemyRepository


def bootstrap_di() -> None:
    di[UserRepository] = UserSqlachemyRepository()

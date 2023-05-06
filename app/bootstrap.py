# -*- coding: utf-8 -*-
from kink import di

from app.user.domain.repositories import UserRepository
from app.user.infra.repositories import UserSqlachemyRepository


def bootstrap_di() -> None:
    di[UserRepository] = UserSqlachemyRepository()

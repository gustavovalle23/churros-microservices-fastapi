# -*- coding: utf-8 -*-
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton

from src.user.infra.repositories.user import UserSqlachemyRepository


class Container(DeclarativeContainer):
    repository_user_sqlalchemy = Singleton(UserSqlachemyRepository)

# -*- coding: utf-8 -*-
from kink import di

from app.user.domain.contracts.repositories import UserRepository
from app.user.domain.contracts.gateways import SyncCloud
from app.user.infra.repositories import UserSqlachemyRepository
from app.user.infra.gateways.cloud_sync import SyncCloudService


def bootstrap_di() -> None:
    di[UserRepository] = UserSqlachemyRepository()
    di[SyncCloud] = SyncCloudService()

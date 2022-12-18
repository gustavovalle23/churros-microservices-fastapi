# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest.mock import patch

from src.__seedwork.application.use_cases import UseCase
from src.user.application.usecases.create.create_user_use_case import CreateUserUseCase
from src.infra.user.repositories.user import UserSqlachemyRepository


class TestCreateUserUseCaseUnit(TestCase):
    use_case: CreateUserUseCase
    user_repository: UserSqlachemyRepository

    def setUp(self) -> None:
        self.user_repository = UserSqlachemyRepository()
        self.use_case = CreateUserUseCase(self.user_repository)


    def test_if_is_instance_of_use_case_class(self):
        self.assertIsInstance(self.use_case, UseCase)

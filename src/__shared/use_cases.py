# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import TypeVar, Generic


Input = TypeVar("Input")
Output = TypeVar("Output")


class UseCase(Generic[Input, Output], ABC):
    @abstractmethod
    def execute(self, input: Input) -> Output:
        raise NotImplementedError()

# -*- coding: utf-8 -*-
from abc import ABC
from dataclasses import dataclass


@dataclass
class Entity(ABC):

    id: str

    @property
    def id(self):
        return str(self.id)
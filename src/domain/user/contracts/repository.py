# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session
from abc import ABC
from typing import List

from src.domain.user.entity.user import User


class UserRepository(ABC):
    def find_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        pass

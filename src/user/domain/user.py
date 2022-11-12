# -*- coding: utf-8 -*-
from datetime import datetime
from uuid import UUID as uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: uuid
    name: str
    email: str
    password: str
    active: bool
    created_at: datetime
    updated_at: datetime = None

# -*- coding: utf-8 -*-
import re
from typing import Optional
from pydantic import BaseModel, validator


regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


class CreateUserInput(BaseModel):
    name: str
    email: str
    active: bool = True
    password: str

    @validator("email")
    @classmethod
    def check_email(cls, value):
        if not re.fullmatch(regex, value):
            raise ValueError("Invalid e-mail")
        return value


class UpdateUserInput(BaseModel):
    id: str
    email: Optional[str] = None
    name: Optional[str] = None

    @validator("email")
    @classmethod
    def check_email(cls, value):
        if not re.fullmatch(regex, value):
            raise ValueError("Invalid e-mail")
        return value

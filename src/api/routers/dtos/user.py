# -*- coding: utf-8 -*-
import re
from typing import Optional
from pydantic import BaseModel, validator


email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


class CreateUserInput(BaseModel):
    name: str
    email: str
    password: str
    active: bool = True

    @validator("email")
    @classmethod
    def check_email(cls, value):
        if not re.fullmatch(email_regex, value):
            raise ValueError("Invalid e-mail")
        return value

    class Config:
        validate_assignment = True


class FindUserInput(BaseModel):
    id: int

    class Config:
        validate_assignment = True


class FindUsersInput(BaseModel):
    limit: int
    skip: int

    class Config:
        validate_assignment = True


class UpdateUserInput(BaseModel):
    id: int
    email: Optional[str] = None
    name: Optional[str] = None

    @validator("email")
    @classmethod
    def check_email(cls, value):
        if not re.fullmatch(email_regex, value):
            raise ValueError("Invalid e-mail")
        return value

    class Config:
        validate_assignment = True


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    active: bool

    class Config:
        validate_assignment = True


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        validate_assignment = True

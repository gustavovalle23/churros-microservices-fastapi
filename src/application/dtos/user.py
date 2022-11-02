# -*- coding: utf-8 -*-
from pydantic import BaseModel


class CreateUserInput(BaseModel):
    name: str
    email: str
    active: bool = True
    password: str


class UpdateUserInput(BaseModel):
    email: str
    active: bool = True

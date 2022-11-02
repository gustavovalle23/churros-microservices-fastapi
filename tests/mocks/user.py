# -*- coding: utf-8 -*-
from uuid import uuid1 as uuid


users = [
    {
        "id": "111111111111111111111111",
        "name": "admin",
        "email": "admin@gmail.com",
        "password": "$2a$12$liEWsKidIhxfxne.g9s1wOrZFh/4KU2mmTLMN3NOa0rjL3797F942",  # admin
        "active": True,
    }
]


users += [
    {
        "id": uuid().hex,
        "name": f"admin{user_order}",
        "email": f"admin{user_order}@gmail.com",
        "password": "$2a$12$liEWsKidIhxfxne.g9s1wOrZFh/4KU2mmTLMN3NOa0rjL3797F942",  # admin
        "active": True,
    }
    for user_order in range(1, 16)
]

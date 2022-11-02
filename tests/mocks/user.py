# -*- coding: utf-8 -*-
from uuid import uuid1 as uuid


users = [
    {
        "id": uuid().hex,
        "name": "admin1",
        "email": "admin@gmail.com",
        "password": "$2a$12$liEWsKidIhxfxne.g9s1wOrZFh/4KU2mmTLMN3NOa0rjL3797F942",  # admin
        "active": True,
    },
    {
        "id": uuid().hex,
        "name": "admin2",
        "email": "admin2@gmail.com",
        "password": "$2a$12$liEWsKidIhxfxne.g9s1wOrZFh/4KU2mmTLMN3NOa0rjL3797F942",  # admin
        "active": True,
    },
]

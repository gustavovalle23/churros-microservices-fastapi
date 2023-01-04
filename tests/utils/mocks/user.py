# -*- coding: utf-8 -*-

# admin
password = "$2a$12$liEWsKidIhxfxne.g9s1wOrZFh/4KU2mmTLMN3NOa0rjL3797F942"

users = [
    {
        "id": int(user_order),
        "name": f"admin{user_order}",
        "email": f"admin{user_order}@gmail.com",
        "password": password,
        "active": True,
    }
    for user_order in range(1, 16)
]

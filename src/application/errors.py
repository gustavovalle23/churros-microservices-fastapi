# -*- coding: utf-8 -*-
from fastapi import status, HTTPException


class UserNotFound:
    def __init__(self) -> None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            [
                {
                    "loc": ["param", "user_id"],
                    "msg": "User not found",
                    "type": "not_found_error",
                }
            ],
        )


class EmailAlreadyRegistered:
    def __init__(self) -> None:
        raise HTTPException(
            status.HTTP_412_PRECONDITION_FAILED,
            [
                {
                    "loc": ["param", "email"],
                    "msg": "Email already registered",
                    "type": "already_registered_error",
                }
            ],
        )


class InvalidEmailPasswordMatch:
    def __init__(self) -> None:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            [
                {
                    "loc": ["param", "password"],
                    "msg": "Invalid Credentials",
                    "type": "invalid_credentials",
                }
            ],
        )

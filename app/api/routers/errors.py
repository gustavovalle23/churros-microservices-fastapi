# -*- coding: utf-8 -*-
from fastapi import status, HTTPException


class UserNotFound:
    @staticmethod
    def _raise() -> HTTPException:
        return HTTPException(
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
    @staticmethod
    def _raise() -> HTTPException:
        return HTTPException(
            status.HTTP_412_PRECONDITION_FAILED,
            [
                {
                    "loc": ["param", "email"],
                    "msg": "Email already registered",
                    "type": "already_registered_error",
                }
            ],
        )


class IncorrectUsernameOrPassword:
    def __init__(self) -> None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

# -*- coding: utf-8 -*-
from dotenv import dotenv_values
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from src.user.infra.repositories import UserSqlachemyRepository

user_repository = UserSqlachemyRepository()


envs = dotenv_values(".env")
SECRET_KEY = envs["SECRET_KEY"]
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate_user(username: str, password: str):
    user = user_repository.find_by_email(username)
    if not user or not pwd_context.verify(password, user.password):
        return False
    return user

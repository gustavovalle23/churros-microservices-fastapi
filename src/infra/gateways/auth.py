# -*- coding: utf-8 -*-
from jose import jwt, JWTError
from src.domain.user import User
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException

from src.infra.database import get_db
from src.infra.gateways.jwt import ALGORITHM, SECRET_KEY
from src.infra.repositories import user as user_repository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = user_repository.find_by_email(db, username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.active == False:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
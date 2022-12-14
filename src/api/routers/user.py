# -*- coding: utf-8 -*-
from kink import di
from datetime import timedelta
from typing import Tuple, Optional
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm as OAuthForm

from src.user.domain.entities import User
from src.database.models import get_db
from src.api.routers.errors import UserNotFound, EmailAlreadyRegistered
from src.api.routers.dtos.user import CreateUserInput, UpdateUserInput, Token
from src.user.infra.gateways.jwt import (
    authenticate_user,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
)
from src.user.infra.gateways.auth import get_current_active_user
from src.user.application.usecases.create.create_user_use_case import CreateUserUseCase
from src.user.domain.repositories import UserRepository

router = APIRouter()

user_repository: UserRepository = di[UserRepository]
create_user_use_case = CreateUserUseCase(user_repository)


@router.get("/users", tags=["users"])
async def find_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users: Tuple[User] = user_repository.find_all(db, skip, limit)
    return {"users": users}


@router.get("/users/{user_id}", tags=["users"])
async def find_user(user_id: int, db: Session = Depends(get_db)):
    user: Optional[User] = user_repository.find_by_id(db, user_id)
    if not user:
        return UserNotFound()
    return {"user": user}


@router.post("/users", tags=["users"], status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserInput, db: Session = Depends(get_db)):
    user_created = create_user_use_case.execute(user, db)
    return {"user": user_created}


@router.post("/users/inactivate", tags=["users"])
async def inactivate_user(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)
):
    user: Optional[User] = user_repository.find_by_id(db, current_user.id)
    if not user:
        return UserNotFound()

    user_repository.inactivate(db, current_user.id)
    return {"message": "inactivated"}


@router.patch("/users", tags=["users"])
async def update_user(input: UpdateUserInput, db: Session = Depends(get_db)):
    user: Optional[User] = user_repository.find_by_id(db, input.id)
    if not user:
        return UserNotFound()

    if user_repository.find_by_email(db, input.email):
        return EmailAlreadyRegistered()

    updated_user = user_repository.update(db, input)
    return {"message": "updated", "user": updated_user}


@router.delete("/users", tags=["users"])
async def delete_user(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    user: Optional[User] = user_repository.find_by_id(db, current_user.id)
    if not user:
        return UserNotFound()

    user_repository.delete(db, current_user.id)
    return {"message": "deleted"}


@router.post("/token", response_model=Token, tags=["users"])
async def login(form_data: OAuthForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

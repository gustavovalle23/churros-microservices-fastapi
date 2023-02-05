# -*- coding: utf-8 -*-
from kink import di
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm as OAuthForm

from src.core.database.models import get_db, db_session
from src.user.domain.entities import User
from src.user.domain.repositories import UserRepository
from src.user.infra.gateways.auth import get_current_active_user
from src.api.routers.dtos.user import (
    CreateUserInput,
    FindUserInput,
    FindUsersInput,
    UpdateUserInput,
    Token,
)
from src.user.application.usecases import (
    CreateUserUseCase,
    FindUserUseCase,
    UpdateUserUseCase,
    FindUsersUseCase,
    InactivateUserUseCase,
    DeleteUserUseCase,
    LoginUserUseCase,
)


router = APIRouter()

user_repository: UserRepository = di[UserRepository]
create_user_use_case = CreateUserUseCase(user_repository)
find_user_use_case = FindUserUseCase(user_repository)
find_users_use_case = FindUsersUseCase(user_repository)
inactivate_user_use_case = InactivateUserUseCase(user_repository)
update_user_use_case = UpdateUserUseCase(user_repository)
delete_user_use_case = DeleteUserUseCase(user_repository)
login_user_use_case = LoginUserUseCase(user_repository)


@router.get("/users", tags=["users"])
async def find_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_session.set(db)
    users = find_users_use_case.prepare_input(skip, limit).execute()
    return {"users": users.users}


@router.get("/users/{user_id}", tags=["users"])
async def find_user(user_id: int, db: Session = Depends(get_db)):
    db_session.set(db)
    input_use_case = FindUserInput(id=user_id)
    user = find_user_use_case.execute(input_use_case)
    return {"user": user}


@router.post("/users", tags=["users"], status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserInput, db: Session = Depends(get_db)):
    db_session.set(db)
    user_created = create_user_use_case.execute(user)
    return {"user": user_created}


@router.post("/users/inactivate", tags=["users"])
async def inactivate_user(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)
):
    db_session.set(db)
    inactivate_user_use_case.execute(current_user)

    return {"message": "inactivated"}


@router.patch("/users", tags=["users"])
async def update_user(input: UpdateUserInput, db: Session = Depends(get_db)):
    db_session.set(db)
    updated_user = update_user_use_case.execute(input)

    return {"user": updated_user}


@router.delete("/users", tags=["users"])
async def delete_user(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    db_session.set(db)
    delete_user_use_case.execute(current_user)

    return {"message": "deleted"}


@router.post("/token", response_model=Token, tags=["users"])
async def login(form_data: OAuthForm = Depends(), db: Session = Depends(get_db)):
    db_session.set(db)
    access_token = login_user_use_case.execute(form_data).access_token

    return {"access_token": access_token, "token_type": "bearer"}

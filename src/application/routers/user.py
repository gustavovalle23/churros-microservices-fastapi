# -*- coding: utf-8 -*-
import bcrypt
from typing import Tuple
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from src.domain.user import User
from src.infra.database import get_db
from src.infra.repositories import user as user_repository
from src.application.dtos.user import CreateUserInput, UpdateUserInput


router = APIRouter()


@router.get("/users", tags=["users"])
async def find_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users: Tuple[User] = user_repository.find_all(db, skip, limit)
    return {"users": users}


@router.get("/users/{user_id}", tags=["users"])
async def find_user(user_id: int, db: Session = Depends(get_db)):
    user: User = user_repository.find_by_id(db, user_id)
    return user


@router.post("/users", tags=["users"], status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserInput, db: Session = Depends(get_db)):
    user.password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_created = user_repository.save(db, user)
    return {"user": user_created}


@router.post("/users/inactivate/{user_id}", tags=["users"])
async def inactivate_user(user_id: int, db: Session = Depends(get_db)):
    user_repository.inactivate(db, user_id)
    return {"message": "inactivated"}


@router.post("/users/{user_id}", tags=["users"])
async def update_user(
    user_id: int, user: UpdateUserInput, db: Session = Depends(get_db)
):
    user_repository.update(db, user_id, user)
    return {"message": "updated"}


@router.delete("/users/{user_id}", tags=["users"])
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_repository.delete(db, user_id)
    return {"message": "deleted"}

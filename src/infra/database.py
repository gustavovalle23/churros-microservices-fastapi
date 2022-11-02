# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from dotenv import dotenv_values
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, Column, String, Boolean, DateTime
from datetime import datetime

envs = dotenv_values(".env")

engine = create_engine(envs["DATABASE_URL"])
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserModel(Base):
    __tablename__ = "user"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(255), nullable=False)
    email: str = Column(String(255), unique=True, nullable=False)
    password: str = Column(String(255))
    active: bool = Column(Boolean(), default=True)
    created_at: datetime = Column(
        DateTime(timezone=True), server_default=datetime.utcnow(), nullable=False
    )
    updated_at: datetime = Column(
        DateTime(timezone=True),
        server_default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
    )

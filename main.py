# -*- coding: utf-8 -*-
from fastapi import FastAPI

from src.user.infra.database import Base, engine
from src.user.infra.routers.user import router as router_users

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router_users)

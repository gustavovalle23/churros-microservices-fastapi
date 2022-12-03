# -*- coding: utf-8 -*-
from fastapi import FastAPI
import uvicorn

from src.infra.database import Base, engine
from src.infra.api.routers.user import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(app)

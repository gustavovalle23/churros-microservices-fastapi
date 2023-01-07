# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI

from src.api.routers.user import router
from src.api.resolvers.schema import graphql_app
from src.core.database.models import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run(app)

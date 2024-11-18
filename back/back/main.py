from fastapi import FastAPI
import json
import db

from routers import user, community

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

db.mongo_connect()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.api_route("soon/v1/")
app.include_router(user.router)
app.include_router(community.router)

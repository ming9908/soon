from fastapi import FastAPI
import json

# from repository import user
from controller import user as con


app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/user")
async def postUser(item: con.PostUser):
    return con.postuser(item)


@app.post("/login")
async def login(item: con.LoginUser):
    return con.login(item)


@app.get("/user")
async def getUser():
    return {"message": "Hello World"}


@app.delete("/user/:user_code")
async def deleteUser(user_code: str):
    return {"message": "Hello World"}

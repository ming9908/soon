from fastapi import FastAPI
import json

# from repository import user
from controller import user as con


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/user")
async def postUser(item: con.PostUser):
    return con.postuser(item)


@app.post("/login")
async def login():
    return con.login()


@app.get("/user")
async def getUser():
    return {"message": "Hello World"}


@app.delete("/user/:user_id")
async def deleteUser():
    return {"message": "Hello World"}

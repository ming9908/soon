from fastapi import APIRouter
from services import user as con

router = APIRouter()


@router.post("/user")
async def postUser(item: con.PostUser):
    await con.postuser(item)
    return


@router.post("/login")
async def login(item: con.LoginUser):
    return con.login(item)


@router.get("/user")
async def getUser():
    return {"message": "Hello World"}


@router.delete("/user/:user_code")
async def deleteUser(user_code: str):
    return {"message": "Hello World"}

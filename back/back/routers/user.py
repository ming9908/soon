from services import user as con
from fastapi import APIRouter

router = APIRouter()


@router.post("/user")
async def postUser(item: con.PostUser):
    res = await con.postuser(item)
    return res


@router.post("/login")
async def login(item: con.LoginUser):
    res = await con.login(item)
    return res


@router.get("/user")
async def getUser():
    return {"message": "Hello World"}


@router.delete("/user/:user_code")
async def deleteUser(user_code: str):
    return {"message": "Hello World"}

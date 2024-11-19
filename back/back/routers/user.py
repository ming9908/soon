from services import user as con
from fastapi import APIRouter


router = APIRouter()


@router.get("/user")
async def getUser():
    return {"message": "Hello World"}


@router.delete("/user/:user_code")
async def deleteUser(user_code: str):
    return {"message": "Hello World"}

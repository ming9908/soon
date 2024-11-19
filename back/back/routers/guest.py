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

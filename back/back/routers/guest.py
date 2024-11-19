from services import user as con
from fastapi import APIRouter


router = APIRouter(tags=["Guest"])


# 회원가입
@router.post("/user")
async def post_user(item: con.PostUser):
    res = await con.post_user(item)
    return res


# user_id check
@router.get("/user/check")
async def postUser(user_id: str):
    res = await con.check_user_id(user_id)
    return res


# login
@router.post("/login")
async def login(item: con.LoginUser):
    res = await con.login(item)
    return res


"""
- 비밀번호 챶기에 대해...

"""

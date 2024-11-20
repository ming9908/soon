from services import user as svc
from fastapi import APIRouter


router = APIRouter(tags=["Guest"])


# 회원가입
@router.post("/user")
async def post_user(item: svc.PostUser):
    res = await svc.post_user(item)
    return res


# user_id check
@router.get("/user/check")
async def check_user_id(user_id: str):
    res = await svc.check_user_id(user_id)
    return res


# login
@router.post("/login")
async def login(item: svc.LoginUser):
    res = await svc.login(item)
    return res


"""
- 비밀번호 챶기에 대해...

"""

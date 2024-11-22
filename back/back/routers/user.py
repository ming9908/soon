from services import user as svc
from fastapi import APIRouter, Depends
from core import auth


router = APIRouter(tags=["User"])


# get user data
@router.get("/user")
async def get_user(payload: dict = Depends(auth.verify_token)):
    user_m_id = payload.get("user_m_id")
    res = await svc.get_user(user_m_id)
    return res


# update user data
@router.patch("/user")
async def patch_user(item: svc.PatchUser, payload: dict = Depends(auth.verify_token)):
    user_m_id = payload.get("user_m_id")
    res = await svc.patch_user(item, user_m_id)
    return res


# 회원 탈퇴
@router.delete("/user")
async def delete_user(payload: dict = Depends(auth.verify_token)):
    user_m_id = payload.get("user_m_id")
    res = await svc.delete_user(user_m_id)
    return res

from services import user as con
from fastapi import APIRouter, Depends, HTTPException
from core import auth


router = APIRouter(tags=["User"])


# get user data
@router.get("/user")
async def get_user(item: con.PostUser):
    return


# update user data
@router.patch("/user")
async def patch_user(item: con.PatchUser, payload: dict = Depends(auth.verify_token)):
    m_id = payload.get("m_id")
    if not m_id:
        raise HTTPException(status_code=404, detail="User not found")

    res = await con.patch_user(item, m_id)
    return res


# 회원 탈퇴
@router.delete("/user")
async def delete_user(payload: dict = Depends(auth.verify_token)):
    return {"message": "Hello World"}


"""
내 정보 보기...?

"""

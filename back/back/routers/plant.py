from services import plant as svc
from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException
from core import auth


router = APIRouter(tags=["Plant"])


# get user data
@router.post("/plant")
async def ddd(item: svc.PostPlant, payload: dict = Depends(auth.verify_token)):
    m_id = payload.get("m_id")
    if not m_id:
        raise HTTPException(status_code=404, detail="User not found")

    await svc.post_plant(item, m_id)
    return


"""
식물 생성
-> 식물 검색 (외부 api 사용)

식물 삭제
식물 죽음 or 살리기
식물 수정(prfile, nick, 물 주기)

식물 리스트

"""

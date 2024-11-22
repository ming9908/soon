from services import feed as svc
from fastapi import APIRouter, HTTPException, Depends
from core import auth

router = APIRouter(tags=["Feed"])

"""
@router.get("/feeds")
async def get_feeds(item: svc.CreateFeed):
    # res = await svc.get_feed()
    return  # svc.feeduser(item)


@router.get("/feed")
async def get_feeds(feed_id: str):
    res = await svc.get_feed(feed_id)
    return res


@router.post("/feed")
async def create_feed(item: svc.CreateFeed, payload: dict = Depends(auth.verify_token)):
    user_m_id = payload.get("user_m_id")
    if not user_m_id:
        raise HTTPException(status_code=404, detail="User not found")
    res = await svc.create_feed(item, user_m_id)
    return res


@router.patch("/feed")
async def patch_feed(item: svc.PatchFeed, payload: dict = Depends(auth.verify_token)):
    user_m_id = payload.get("user_m_id")
    if not user_m_id:
        raise HTTPException(status_code=404, detail="User not found")
    res = await svc.patch_feed(item, user_m_id)
    return res


@router.delete("/feed")
async def patch_feed(feed_id: str, payload: dict = Depends(auth.verify_token)):
    user_m_id = payload.get("user_m_id")
    if not user_m_id:
        raise HTTPException(status_code=404, detail="User not found")
    res = await svc.delete_feed(feed_id, user_m_id)
    return res
"""

from services import post as svc
from fastapi import APIRouter, Depends
from core import auth

router = APIRouter(tags=["Post"])


@router.get("/posts")
async def get_posts(item: svc.CreatePost):
    # res = await svc.get_post()
    return  # svc.postuser(item)


@router.get("/post")
async def get_posts(post_id: str):
    res = await svc.get_post(post_id)
    return res


@router.post("/post")
async def create_post(item: svc.CreatePost, payload: dict = Depends(auth.verify_token)):
    user_m_id = payload.get("user_m_id")
    res = await svc.create_post(item, user_m_id)
    return res


@router.patch("/post")
async def patch_post(item: svc.PatchPost, payload: dict = Depends(auth.verify_token)):
    user_m_id = payload.get("user_m_id")
    res = await svc.patch_post(item, user_m_id)
    return res


@router.delete("/post")
async def patch_post(post_id: str, payload: dict = Depends(auth.verify_token)):
    user_m_id = payload.get("user_m_id")
    res = await svc.delete_post(post_id, user_m_id)
    return res

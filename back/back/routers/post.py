from services import post as svc
from fastapi import APIRouter, HTTPException, Depends
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
    m_id = payload.get("m_id")
    if not m_id:
        raise HTTPException(status_code=404, detail="User not found")
    res = await svc.create_post(item, m_id)
    return res


@router.patch("/post")
async def patch_post(item: svc.PatchPost, payload: dict = Depends(auth.verify_token)):
    m_id = payload.get("m_id")
    if not m_id:
        raise HTTPException(status_code=404, detail="User not found")
    res = await svc.patch_post(item, m_id)
    return res


@router.delete("/post")
async def patch_post(post_id: str, payload: dict = Depends(auth.verify_token)):
    m_id = payload.get("m_id")
    if not m_id:
        raise HTTPException(status_code=404, detail="User not found")
    res = await svc.delete_post(post_id, m_id)
    return res


"""
- 게시글 작성
- 게시글 수정
- 게시글 보기(단일)
내 게시글 보기 (list)
내가 좋아요한 게시글 보기 (list)  <- 통합? 분리가 맞는거 같음 ( 테이블 분리 예정 )
게시글 보기 (list) topic별로 구분 


- 댓글달기
- 댓글수정
- 댓글삭제

"""

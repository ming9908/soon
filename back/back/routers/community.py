from services import user as con
from fastapi import APIRouter

router = APIRouter(tags=["Community"])


@router.get("/posts")
async def get_posts(item: con.PostUser):
    return con.postuser(item)


@router.get("/posts/my")
async def get_my_posts(item: con.LoginUser):
    return con.login(item)


@router.get("/posts/likey")
async def get_likey_posts():
    return {"message": "Hello World"}


@router.post("/post")
async def deleteUser(user_code: str):
    return {"message": "Hello World"}


"""
- 게시글 작성
- 게시글 수정
- 게시글 보기(단일)
- 내 게시글 보기 (list)          <- 통합?
- 내가 좋아요한 게시글 보기 (list)  <- 통합?
- 게시글 보기 (list) topic별로 구분 


- 댓글달기
- 댓글수정
- 댓글삭제

"""

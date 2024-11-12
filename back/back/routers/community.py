from fastapi import APIRouter
from services import user as con

router = APIRouter()


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

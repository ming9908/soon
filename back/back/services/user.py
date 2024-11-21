from fastapi import HTTPException, status
from pydantic import BaseModel
from core import auth, Response, common
from models import user as db
from datetime import datetime


class PostUser(BaseModel):
    user_id: str
    password: str
    nick: str
    profile: str


async def post_user(item: PostUser):
    # set user data
    user = db.User(**item.model_dump())
    user.set_password(item.password)
    user.set_new_code()

    # insert user
    await db.create_user(user)

    return Response("create user success", None)


async def check_user_id(user_id: str):
    count = await db.count_user_id(user_id)
    if count > 0:
        return Response("", False)
    else:
        return Response("", True)


class PatchUser(BaseModel):
    nick: str
    profile: str


async def patch_user(item: PatchUser, user_m_id: str):
    result = await db.update_user(user_m_id, item)
    if result.modified_count > 0:
        return Response("success", None)
    return Response("update 0", None)


class LoginUser(BaseModel):
    user_id: str
    password: str


async def login(item: LoginUser):
    # user select
    user = await db.find_user_by_user_id(item.user_id)
    if user != None:
        if common.verify_password(item.password, user.password):
            access_token = auth.create_access_token(
                auth.Token(user.m_id, user.user_id, user.nick)
            )
            print(access_token)
            return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


async def delete_user(user_m_id: str):
    result = await db.delete_user(user_m_id)
    if result.deleted_count < 0:
        return Response("delete 0", None)
    return Response("", None)


class ResGetUser(BaseModel):
    user_id: str
    nick: str
    profile: str
    code: str
    create_date: datetime


async def get_user(user_m_id: str):
    user = await db.find_user_by_m_id(user_m_id)
    if user == None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return Response("", ResGetUser(**user.model_dump()))

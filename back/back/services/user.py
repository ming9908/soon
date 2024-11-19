from fastapi import HTTPException, status
from pydantic import BaseModel  # import BaseModel
from core import common, auth
from models import user as user_db


class PostUser(BaseModel):
    user_id: str
    password: str
    nick: str
    profile: str


async def post_user(item: PostUser):
    # set user data
    user = user_db.User(user_id=item.user_id, nick=item.nick, profile=item.profile)
    user.set_password(item.password)
    user.set_new_code()

    # insert user
    await user_db.create_user(user)

    return common.Response("create user success", None)


async def check_user_id(user_id: str):
    count = await user_db.count_user_id(user_id)
    if count > 0:
        return common.Response("", False)
    else:
        return common.Response("", True)


class PatchUser(BaseModel):
    nick: str
    profile: str


async def patch_user(item: PatchUser, m_id: str):
    result = await user_db.patch_user(m_id, item)
    if result.modified_count > 0:
        return common.Response("success", None)
    return common.Response("update 0", None)


class LoginUser(BaseModel):
    user_id: str
    password: str


async def login(item: LoginUser):
    # user select
    user = await user_db.find_user(item.user_id)
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

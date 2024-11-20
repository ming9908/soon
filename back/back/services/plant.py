from fastapi import HTTPException, status
from pydantic import BaseModel
from core import Response
from models import user as user_db


class PostPlant(BaseModel):
    name: str
    nick: str
    profile: str
    # 물주기


async def create_post(item: PostPlant, m_id: str):
    # set user data
    user = user_db.User(user_id=item.user_id, nick=item.nick, profile=item.profile)
    user.set_password(item.password)
    user.set_new_code()

    # insert user
    await user_db.create_user(user)

    return Response("make plant success", None)

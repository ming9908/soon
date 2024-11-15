from pydantic import BaseModel  # import BaseModel
from core import common, auth
from models import user


class PostUser(BaseModel):
    name: str
    nick: str
    profile: str


async def postuser(item: PostUser):
    res = common.response()
    # inser user

    user1 = user.User(name=item.name, nick=item.nick, profile=item.profile)
    await user.create_user(user1)

    res.success = True
    return res


class LoginUser(BaseModel):
    user_id: str
    pw: str


def login(user: LoginUser):
    res = common.response()
    # user select

    # make token
    token = auth.MakeJWTToken("ser.user_id", "user.nick")
    if token == "":
        return res
    res.set_success()

    return res

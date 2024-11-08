from pydantic import BaseModel  # import BaseModel
from auth import auth
from common import response


class PostUser(BaseModel):
    name: str
    nick: str
    profile: str


def postuser(item: PostUser):
    res = response()
    # inser user

    res.success = True
    return res


class LoginUser(BaseModel):
    user_id: str
    pw: str


def login(user: LoginUser):
    res = response()
    # user select

    # make token
    token = auth.MakeJWTToken("ser.user_id", "user.nick")
    if token == "":
        return res
    res.set_success()

    return res

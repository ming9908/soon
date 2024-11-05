from pydantic import BaseModel  # import BaseModel
from auth import auth


class response:
    success: bool
    message: str
    data: any

    def __init__(self):
        self.success = False


class PostUser(BaseModel):
    name: str
    nick: str
    profile: str


def postuser(item: PostUser):
    res = response()
    # inser user

    res.success = True
    return res


class LoginUser:
    user_id: str
    pw: str


def login(user: LoginUser):
    # user select

    # make token
    token = auth.MakeJWTToken("ser.user_id", "user.nick")

    return token

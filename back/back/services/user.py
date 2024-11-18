from fastapi import HTTPException, status
from pydantic import BaseModel  # import BaseModel
from core import common, auth
from models import user as user_db


class PostUser(BaseModel):
    user_id: str
    password: str
    nick: str
    profile: str


async def postuser(item: PostUser):
    res = common.response()

    # set user data
    user = user_db.User(user_id=item.user_id, nick=item.nick, profile=item.profile)
    user.set_password(item.password)
    user.set_new_code()

    # insert user
    await user_db.create_user(user)

    res.success = True
    return res


class LoginUser(BaseModel):
    user_id: str
    password: str


async def login(item: LoginUser):
    res = common.response()
    # user select
    user = await user_db.find_user(item.user_id)
    if user != None:
        if common.verify_password(item.password, user.password):
            print("???")
            access_token = auth.create_access_token(auth.Token(user.user_id, user.nick))
            print(access_token)
            return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

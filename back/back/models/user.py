import db
from fastapi import HTTPException
from pydantic import BaseModel, model_validator
from core import common
from datetime import datetime
from typing import Optional


class User(BaseModel):
    user_id: str
    password: Optional[str] = None
    nick: str
    profile: str
    code: Optional[str] = None
    create_date: Optional[str] = None
    db_stat: str = "A"

    @model_validator(mode="after")
    def set_create_date(cls, values):
        if not values.create_date:  # create_date가 없다면
            values.create_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        return values

    def set_password(self, password):
        self.password = common.get_password_hash(password)

    def set_new_code(self):
        self.code = common.make_user_code()


async def create_user(item: User):
    await db.mongo.db["user"].insert_one(item.model_dump())
    print(f"{item.nick}으로 가입되었습니다.")
    return


async def find_user(user_id: str):
    user = await db.mongo.db["user"].find_one({"user_id": user_id})
    if user is not None:
        return User(**user)
    else:
        print("검색 결과가 없습니다")
        raise HTTPException(status_code=404, detail="User not found")

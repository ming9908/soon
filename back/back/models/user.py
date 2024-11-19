import db
from fastapi import HTTPException
from pydantic import BaseModel, model_validator
from core import common
from datetime import datetime
from typing import Optional
from bson import ObjectId


class User(BaseModel):
    m_id: Optional[str]
    user_id: str
    password: Optional[str] = None
    nick: str
    profile: str
    code: Optional[str] = None
    create_date: Optional[str] = None
    db_stat: str = "A"

    class Config:
        # ObjectId를 str로 변환
        json_encoders = {ObjectId: str}

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
    if user is None:
        print("검색 결과가 없습니다")
        raise HTTPException(status_code=404, detail="User not found")
    if user:
        user["m_id"] = str(user["_id"])
    return User(**user)


async def count_user_id(user_id: str):
    count = await db.mongo.db["user"].count_documents({"user_id": user_id})
    return count


async def patch_user(m_id: str, data):
    update_data = {
        key: value
        for key, value in data.dict(exclude_unset=True).items()
        if value != ""  # 빈 문자열("")을 제외
    }

    # 만약 update_data가 비어있다면, 업데이트할 데이터가 없다는 의미
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid data to update")

    result = await db.mongo.db["user"].update_one(
        {"_id": ObjectId(m_id)}, {"$set": update_data}
    )
    return result

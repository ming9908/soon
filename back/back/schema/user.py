from pydantic import BaseModel, model_validator
from core import common
from datetime import datetime
from typing import Optional
from bson import ObjectId


class User(BaseModel):
    m_id: Optional[str] = None
    user_id: str
    password: Optional[str] = None
    nick: str
    profile: str
    code: Optional[str] = None  # 유저 고유 코드
    create_date: Optional[datetime] = None
    db_stat: str = "A"  # 디비

    class Config:
        # ObjectId를 str로 변환
        json_encoders = {ObjectId: str}

    @model_validator(mode="after")
    def set_create_date(cls, values):
        if not values.create_date:  # create_date가 없다면
            values.create_date = datetime.now()
        return values

    """@model_validator(mode="before")
    def remove_password(cls, values):
        if "password" in values:
            del values["password"]
        return values
    """

    def set_password(self, password):
        self.password = common.get_password_hash(password)

    def set_new_code(self):
        self.code = common.make_user_code()

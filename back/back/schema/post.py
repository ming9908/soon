import db
from fastapi import HTTPException
from pydantic import BaseModel, model_validator
from core import common
from datetime import datetime
from typing import Optional
from bson import ObjectId


class Post(BaseModel):
    m_id: Optional[str] = None

    title: str
    content: str

    user_m_id: Optional[str] = None  # 작성자
    create_date: Optional[datetime] = None  # 작성일
    last_update_date: Optional[datetime] = None  # 마지막 수정일

    db_stat: str = "A"

    class Config:
        json_encoders = {ObjectId: str}

    @model_validator(mode="after")
    def set_create_date(cls, values):
        if not values.create_date:  # create_date가 없다면
            values.create_date = datetime.now()
        if not values.last_update_date:
            values.last_update_date = datetime.now()
        return values

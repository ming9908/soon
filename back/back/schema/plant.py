from pydantic import BaseModel, model_validator
from datetime import datetime
from typing import Optional
from bson import ObjectId


class Plant(BaseModel):
    m_id: Optional[str] = None
    name: Optional[str] = None  # 식물 이름
    nick: str  # 별칭
    profile: str

    user_m_id: Optional[str] = None

    watering_interval: int  # 물 주기
    planted_date: Optional[datetime] = None  # 심은날짜
    status: str = "A"  # 생존여부 alive-"A", dead-"D"

    db_stat: str = "A"

    class Config:
        # ObjectId를 str로 변환
        json_encoders = {ObjectId: str}

    @model_validator(mode="after")
    def set_create_date(cls, values):
        if not values.planted_date:
            values.planted_date = datetime.now()
        return values

from pydantic import BaseModel, model_validator
from datetime import datetime
from typing import Optional
from bson import ObjectId


class Plant(BaseModel):
    m_id: Optional[str] = None
    name: str  # 식물 이름
    nick: str  # 별칭
    profile: str

    user_id: str

    watering_interval: int  # 물 주기
    # 심은날짜
    # 생존여부

    db_stat: str = "A"

    class Config:
        # ObjectId를 str로 변환
        json_encoders = {ObjectId: str}

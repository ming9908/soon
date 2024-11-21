from pydantic import BaseModel, model_validator
from datetime import datetime
from typing import Optional
from bson import ObjectId


class Schedule(BaseModel):
    m_id: Optional[str] = None
    user_m_id: Optional[str] = None
    name: str  # 일정 이름
    type: str  # 일정 타입
    content: str  # 일정 내용

    status: Optional[str] = None  # 일정 상태 미완료 - "A" 완료 - "D"

    target_date: datetime
    db_stat: str = "A"  # 디비

    class Config:
        # ObjectId를 str로 변환
        json_encoders = {ObjectId: str}

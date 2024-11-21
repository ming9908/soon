from fastapi import HTTPException, status
from pydantic import BaseModel
from core import Response
from models import schedule as db
from datetime import datetime


class PostSchedule(BaseModel):
    name: str
    type: str
    content: str
    target_date: datetime


async def create_schedule(item: PostSchedule, user_m_id: str):
    schedule = db.Schedule(**item.model_dump())
    await db.create_schedule(schedule, user_m_id)
    return Response("make schedule success", None)


async def get_schedule(schedule_id: str):
    schedule = await db.get_schedule(schedule_id)
    return Response("", schedule)


async def get_schedules(user_m_id: str):
    schedules = await db.get_schedules(user_m_id)
    return Response("", schedules)


class PatchSchedule(BaseModel):
    schedule_id: str
    name: str
    type: str
    content: str
    target_date: datetime


async def patch_schedule(item: PatchSchedule, user_m_id: str):
    schedule = db.Schedule(**item.model_dump())
    schedule.m_id = item.schedule_id

    result = await db.update_schedule(schedule, user_m_id)
    if result.modified_count > 0:
        return Response("success", None)
    return Response("modify 0", None)


class PatchStatus(BaseModel):
    schedule_id: str
    status: str


async def patch_schedule_status(item: PatchStatus, user_m_id: str):
    result = await db.update_schedule_status(item.schedule_id, item.status, user_m_id)
    if result.modified_count > 0:
        return Response("success", None)
    return Response("modify 0", None)


async def delete_schedule(schedule_id: str, user_m_id: str):
    result = await db.delete_schedule(schedule_id, user_m_id)
    if result.modified_count > 0:
        return Response("success", None)
    return Response("modify 0", None)

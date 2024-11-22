from services import schedule as svc
from fastapi import APIRouter, Depends
from core import auth

router = APIRouter(tags=["Schedule"])


@router.post("/schedule")
async def post_schedule(
    item: svc.PostSchedule, payload: dict = Depends(auth.verify_token)
):
    user_m_id = payload.get("user_m_id")
    res = await svc.create_schedule(item, user_m_id)
    return res


@router.get("/schedule")
async def get_schedule(schedule_id: str):
    res = await svc.get_schedule(schedule_id)
    return res


@router.get("/schedules")
async def get_schedules(payload: dict = Depends(auth.verify_token)):
    user_m_id = payload.get("user_m_id")
    res = await svc.get_schedules(user_m_id)
    return res


@router.patch("/schedule")
async def patch_schedule(
    item: svc.PatchSchedule, payload: dict = Depends(auth.verify_token)
):
    user_m_id = payload.get("user_m_id")
    res = await svc.patch_schedule(item, user_m_id)
    return res


@router.patch("/schedule/status")
async def patch_schedule_status(
    item: svc.PatchStatus, payload: dict = Depends(auth.verify_token)
):
    user_m_id = payload.get("user_m_id")
    res = await svc.patch_schedule_status(item, user_m_id)
    return res


@router.delete("/schedule")
async def delete_schedule(schedule_id: str, payload: dict = Depends(auth.verify_token)):
    user_m_id = payload.get("user_m_id")
    res = await svc.delete_schedule(schedule_id, user_m_id)
    return res

from services import plant as svc
from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException
from core import auth


router = APIRouter(tags=["Plant"])


@router.post("/plant")
async def post_plant(item: svc.PostPlant, payload: dict = Depends(auth.verify_token)):
    user_m_id = payload.get("user_m_id")
    if not user_m_id:
        raise HTTPException(status_code=404, detail="User not found")

    res = await svc.post_plant(item, user_m_id)
    return res


@router.patch("/plant")
async def patch_plant(item: svc.PatchPlant, payload: dict = Depends(auth.verify_token)):
    user_m_id = payload.get("user_m_id")
    if not user_m_id:
        raise HTTPException(status_code=404, detail="User not found")

    res = await svc.patch_plant(item, user_m_id)
    return res


@router.patch("/plant/status")
async def patch_plant(
    item: svc.PatchPlantStatus, payload: dict = Depends(auth.verify_token)
):
    user_m_id = payload.get("user_m_id")
    if not user_m_id:
        raise HTTPException(status_code=404, detail="User not found")

    res = await svc.patch_plant_status(item, user_m_id)
    return res


@router.get("/plant")
async def get_plant(plant_id: str):
    res = await svc.get_plant(plant_id)
    return res


@router.get("/plants")
async def get_plants(payload: dict = Depends(auth.verify_token)):
    user_m_id = payload.get("user_m_id")
    if not user_m_id:
        raise HTTPException(status_code=404, detail="User not found")

    res = await svc.get_plants(user_m_id)
    return res

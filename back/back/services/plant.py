from fastapi import HTTPException, status
from pydantic import BaseModel
from core import Response
from models import plant as db


class PostPlant(BaseModel):
    name: str
    nick: str
    profile: str
    watering_interval: int  # 물주기


async def post_plant(item: PostPlant, user_m_id: str):
    plant = db.Plant(**item.model_dump())
    await db.create_plant(plant, user_m_id)
    return Response("make plant success", None)


class PatchPlant(BaseModel):
    plant_id: str
    nick: str
    profile: str
    watering_interval: int  # 물주기


async def patch_plant(item: PatchPlant, user_m_id: str):
    plant = db.Plant(**item.model_dump())
    plant.m_id = item.plant_id

    result = await db.update_plant(plant, user_m_id)
    if result.modified_count > 0:
        return Response("success", None)
    return Response("modify 0", None)


class PatchPlantStatus(BaseModel):
    plant_id: str
    status: str


async def patch_plant_status(item: PatchPlantStatus, user_m_id: str):
    result = await db.update_plant_status(item.plant_id, item.status, user_m_id)
    if result.modified_count > 0:
        return Response("success", None)
    return Response("modify 0", None)


async def get_plant(plant_id: str):
    plant = await db.get_plant(plant_id)
    return Response("", plant)


async def get_plants(user_m_id: str):
    plants = await db.get_plants(user_m_id)
    return Response("", plants)

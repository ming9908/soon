from schema import Plant
import db
from fastapi import HTTPException, status
from bson import ObjectId
from . import serialize_item


async def create_plant(item: Plant, user_m_id: str):
    item.user_m_id = user_m_id
    await db.mongo.db["plant"].insert_one(item.model_dump(exclude={"m_id"}))
    return


async def update_plant(item: Plant, user_m_id: str):
    update_data = {
        key: value
        for key, value in item.model_dump(
            exclude={"m_id", "planted_date"}, exclude_unset=True
        ).items()
        if value != ""  # 빈 문자열("")을 제외
    }

    if not update_data:
        raise HTTPException(status_code=400, detail="No valid data to update")

    try:
        result = await db.mongo.db["plant"].update_one(
            {"_id": ObjectId(item.m_id), "user_m_id": user_m_id}, {"$set": update_data}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid ObjectId format: {str(e)}",
        )

    return result


async def update_plant_status(plant_id: str, status: str, user_m_id: str):
    try:
        result = await db.mongo.db["plant"].update_one(
            {"_id": ObjectId(plant_id), "user_m_id": user_m_id},
            {"$set": {"status": status}},
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid ObjectId format: {str(e)}",
        )

    return result


async def get_plant(plant_id: str):
    try:
        plant = await db.mongo.db["plant"].find_one(
            {"_id": ObjectId(plant_id), "db_stat": "A"}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid ObjectId format: {str(e)}",
        )
    if plant is None:
        print("검색 결과가 없습니다")
        raise HTTPException(status_code=404, detail="User not found")
    if plant:
        plant["m_id"] = str(plant["_id"])
    return Plant(**plant)


async def get_plants(user_m_id: str):
    plants = (
        await db.mongo.db["plant"]
        .find({"user_m_id": user_m_id, "db_stat": "A"})
        .to_list()
    )
    if plants is None:
        print("검색 결과가 없습니다")
        raise HTTPException(status_code=404, detail="User not found")
    plt = [serialize_item(item) for item in plants]
    return [Plant(**item) for item in plt]

import db
from bson import ObjectId
from schema import Schedule
from . import serialize_item
import core


async def create_schedule(item: Schedule, m_id):
    item.user_m_id = m_id
    await db.mongo.db["schedule"].insert_one(item.model_dump(exclude={"m_id"}))
    return


async def get_schedule(schedule_id: str):
    try:
        schedule = await db.mongo.db["schedule"].find_one(
            {"_id": ObjectId(schedule_id), "db_stat": "A"}
        )
    except Exception as e:
        core.raise_bad_request(f"Invalid ObjectId format: {str(e)}")
    if schedule is None:
        print("검색 결과가 없습니다")
        core.raise_not_found("schedule not found")
    if schedule:
        schedule["m_id"] = str(schedule["_id"])
    return Schedule(**schedule)


async def get_schedules(user_m_id: str):
    schedules = (
        await db.mongo.db["schedule"]
        .find({"user_m_id": user_m_id, "db_stat": "A"})
        .to_list()
    )
    if schedules is None:
        return []
    sch = [serialize_item(item) for item in schedules]
    return [Schedule(**item) for item in sch]


async def update_schedule(item: Schedule, user_m_id: str):
    update_data = {
        key: value
        for key, value in item.model_dump(exclude="m_id", exclude_unset=True).items()
        if value != ""
    }

    if not update_data:
        # 로그처리
        print("no valid data to update")

    try:
        result = await db.mongo.db["schedule"].update_one(
            {"_id": ObjectId(item.m_id), "user_m_id": user_m_id}, {"$set": update_data}
        )
    except Exception as e:
        core.raise_bad_request(f"Invalid ObjectId format: {str(e)}")

    return result


async def update_schedule_status(schedule_id: str, status: str, user_m_id: str):
    try:
        result = await db.mongo.db["schedule"].update_one(
            {"_id": ObjectId(schedule_id), "user_m_id": user_m_id},
            {"$set": {"status": status}},
        )
    except Exception as e:
        core.raise_bad_request(f"Invalid ObjectId format: {str(e)}")

    return result


async def delete_schedule(schedule_id: str, user_m_id: str):
    try:
        result = await db.mongo.db["schedule"].update_one(
            {"_id": ObjectId(schedule_id), "user_m_id": user_m_id},
            {"$set": {"db_stat": "D"}},
        )
    except Exception as e:
        core.raise_bad_request(f"Invalid ObjectId format: {str(e)}")

    return result

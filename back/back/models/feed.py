import db
from bson import ObjectId
from schema import Feed

"""

async def create_feed(item: Feed, m_id):
    item.user_m_id = m_id
    await db.mongo.db["feed"].insert_one(item.model_dump(exclude={"m_id"}))
    return


async def get_feed(feed_id: str):
    try:
        feed = await db.mongo.db["feed"].find_one({"_id": ObjectId(feed_id)})
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid ObjectId format: {str(e)}",
        )
    if feed is None:
        print("검색 결과가 없습니다")
        raise HTTPException(status_code=404, detail="User not found")
    if feed:
        feed["m_id"] = str(feed["_id"])
    return Feed(**feed)


async def update_feed(item: Feed, m_id):
    update_data = {
        key: value
        for key, value in item.model_dump(
            exclude="create_date", exclude_unset=True
        ).items()
        if value != ""  # 빈 문자열("")을 제외
    }

    if not update_data:
        raise HTTPException(status_code=400, detail="No valid data to update")

    try:
        result = await db.mongo.db["feed"].update_one(
            {"_id": ObjectId(item.m_id), "user_m_id": m_id}, {"$set": update_data}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid ObjectId format: {str(e)}",
        )

    return result


async def delete_feed(feed_id: str, m_id: str):
    try:
        result = await db.mongo.db["feed"].delete_one(
            {"_id": ObjectId(feed_id), "user_m_id": m_id}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid ObjectId format: {str(e)}",
        )
    return result
"""

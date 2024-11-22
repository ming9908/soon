import db
from bson import ObjectId
from schema import Post
import core


async def create_post(item: Post, user_m_id):
    item.user_m_id = user_m_id
    await db.mongo.db["post"].insert_one(item.model_dump(exclude={"m_id"}))
    return


async def get_post(post_id: str):
    try:
        post = await db.mongo.db["post"].find_one(
            {"_id": ObjectId(post_id), "db_stat": "A"}
        )
    except Exception as e:
        core.raise_bad_request(f"Invalid ObjectId format: {str(e)}")
    if post is None:
        print("검색 결과가 없습니다")
        core.raise_not_found("post not found")
    if post:
        post["m_id"] = str(post["_id"])
    return Post(**post)


async def update_post(item: Post, user_m_id):
    update_data = {
        key: value
        for key, value in item.model_dump(
            exclude={"m_id", "create_date"}, exclude_unset=True
        ).items()
        if value != ""  # 빈 문자열("")을 제외
    }

    if not update_data:
        # raise HTTPException(status_code=400, detail="No valid data to update")
        # 로그
        print("no valid data to update")

    try:
        result = await db.mongo.db["post"].update_one(
            {"_id": ObjectId(item.m_id), "user_m_id": user_m_id}, {"$set": update_data}
        )
    except Exception as e:
        core.raise_bad_request(f"Invalid ObjectId format: {str(e)}")

    return result


async def delete_post(post_id: str, user_m_id: str):
    try:
        # result = await db.mongo.db["post"].delete_one({"_id": ObjectId(post_id), "user_m_id": user_m_id})
        result = await db.mongo.db["post"].update_one(
            {"_id": ObjectId(post_id), "user_m_id": user_m_id},
            {"$set": {"db_stat": "D"}},
        )
    except Exception as e:
        core.raise_bad_request(f"Invalid ObjectId format: {str(e)}")
    return result

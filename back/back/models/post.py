import db
from fastapi import HTTPException, status
from bson import ObjectId
from schema import Post


async def create_post(item: Post, m_id):
    item.user_m_id = m_id
    await db.mongo.db["post"].insert_one(item.model_dump(exclude={"m_id"}))
    print(f"{item.title}으로 가입되었습니다.")
    return


async def get_post(post_id: str):
    try:
        post = await db.mongo.db["post"].find_one({"_id": ObjectId(post_id)})
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid ObjectId format: {str(e)}",
        )
    if post is None:
        print("검색 결과가 없습니다")
        raise HTTPException(status_code=404, detail="User not found")
    if post:
        post["m_id"] = str(post["_id"])
    return Post(**post)


async def update_post(item: Post, m_id):
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
        result = await db.mongo.db["post"].update_one(
            {"_id": ObjectId(item.m_id), "user_m_id": m_id}, {"$set": update_data}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid ObjectId format: {str(e)}",
        )

    return result


async def delete_post(post_id: str, m_id: str):
    try:
        result = await db.mongo.db["post"].delete_one(
            {"_id": ObjectId(post_id), "user_m_id": m_id}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid ObjectId format: {str(e)}",
        )
    return result

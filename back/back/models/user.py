import db
from fastapi import HTTPException, status
from bson import ObjectId
from schema import User


async def create_user(item: User):
    await db.mongo.db["user"].insert_one(item.model_dump(exclude={"m_id"}))
    print(f"{item.nick}으로 가입되었습니다.")
    return


async def find_user_by_user_id(user_id: str):
    user = await db.mongo.db["user"].find_one({"user_id": user_id, "db_stat": "A"})
    if user is None:
        print("검색 결과가 없습니다")
        raise HTTPException(status_code=404, detail="User not found")
    if user:
        user["m_id"] = str(user["_id"])
    return User(**user)


async def find_user_by_m_id(m_id: str):
    try:
        user = await db.mongo.db["user"].find_one(
            {"_id": ObjectId(m_id), "db_stat": "A"}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid ObjectId format: {str(e)}",
        )
    if user is None:
        print("검색 결과가 없습니다")
        raise HTTPException(status_code=404, detail="User not found")
    if user:
        user["m_id"] = str(user["_id"])
    return User(**user)


async def count_user_id(user_id: str):
    count = await db.mongo.db["user"].count_documents(
        {"user_id": user_id, "db_stat": "A"}
    )
    return count


async def update_user(m_id: str, data):
    update_data = {
        key: value
        for key, value in data.dict(exclude_unset=True).items()
        if value != ""  # 빈 문자열("")을 제외
    }

    # 만약 update_data가 비어있다면, 업데이트할 데이터가 없다는 의미
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid data to update")

    result = await db.mongo.db["user"].update_one(
        {"_id": ObjectId(m_id)}, {"$set": update_data}
    )
    return result


async def delete_user(m_id: str):
    try:
        # result = await db.mongo.db["user"].delete_one({"_id": ObjectId(m_id)})
        result = await db.mongo.db["user"].update_one(
            {"_id": ObjectId(m_id)}, {"$set": {"db_stat": "D"}}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid ObjectId format: {str(e)}",
        )
    return result

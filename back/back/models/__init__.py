def serialize_item(item):
    item["m_id"] = str(item["_id"])  # ObjectId를 문자열로 변환
    return item

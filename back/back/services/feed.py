from fastapi import HTTPException, status
from pydantic import BaseModel
from core import Response
from models import feed as db


class CreateFeed(BaseModel):
    image: list[str]
    content: str


async def post_feed(item: CreateFeed, m_id: str):
    # TODO : 이미지 처리
    feed = db.Feed(**item.model_dump())
    await db.create_feed(feed, m_id)
    return Response("make feed success", None)


async def get_feed(feed_id: str):
    feed = await db.get_feed(feed_id)
    return Response("", feed)


class PatchFeed(BaseModel):
    feed_id: str
    content: str


async def patch_feed(item: PatchFeed, m_id: str):
    feed = db.Feed(**item.model_dump())
    feed.m_id = item.feed_id

    result = await db.update_feed(feed, m_id)
    if result.modified_count > 0:
        return Response("success", None)
    return Response("modify 0", None)


async def delete_feed(feed_id: str, m_id: str):
    result = await db.delete_feed(feed_id, m_id)
    if result.deleted_count > 0:
        return Response("success", None)
    return Response("modify 0", None)


"""
피드 생성시 이미지에 대한 처리
가져올때도 동일
"""

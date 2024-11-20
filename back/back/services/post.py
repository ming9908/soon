from fastapi import HTTPException, status
from pydantic import BaseModel
from core import Response
from models import post as db
from datetime import datetime


class CreatePost(BaseModel):
    title: str
    content: str


async def create_post(item: CreatePost, m_id: str):
    post = db.Post(**item.model_dump())
    await db.create_post(post, m_id)
    return Response("make post success", None)


async def get_post(post_id: str):
    post = await db.get_post(post_id)
    return Response("", post)


class PatchPost(BaseModel):
    post_id: str
    title: str
    content: str


async def patch_post(item: PatchPost, m_id: str):
    post = db.Post(**item.model_dump())
    post.m_id = item.post_id

    result = await db.update_post(post, m_id)
    if result.modified_count > 0:
        return Response("success", None)
    return Response("modify 0", None)


async def delete_post(post_id: str, m_id: str):
    result = await db.delete_post(post_id, m_id)
    if result.deleted_count > 0:
        return Response("success", None)
    return Response("modify 0", None)

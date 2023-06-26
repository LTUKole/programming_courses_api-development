from fastapi import APIRouter
from database.sys_db import SysDb
from database.data_models import Tag, Role, TagUpdate
from typing import Optional

router = APIRouter()


@router.put("/tags/{tags_id}", response_model=TagUpdate)
async def update_tags(tags_id: int, tags: TagUpdate):
    db = SysDb()
    return db.update_tags(tags_id, tags)


@router.get("/tags")
async def get_tags(
    tag_name: Optional[str] = None,
):
    db = SysDb()
    return db.get_tags(tag_name)


@router.get("/roles")
async def get_roles(
    role_type: Optional[str] = None,
):
    db = SysDb()
    return db.get_roles(role_type)


@router.post("/tags/")
async def create_tag(tag: Tag):
    db = SysDb()
    return db.create_tag(tag)


@router.post("/roles/")
async def create_role(role: Role):
    db = SysDb()
    return db.create_role(role)


@router.delete("/tags/{tag_id}")
async def delete_tag(tag_id: int):
    db = SysDb()
    return db.delete_tag(tag_id)


@router.delete("/roles/{role_id}")
async def delete_role(role_id: int):
    db = SysDb()
    return db.delete_role(role_id)

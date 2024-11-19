from fastapi import APIRouter
from services import user as con
from . import user, community


router = APIRouter(prefix="/soon/v1")
router.include_router(user.router)
router.include_router(community.router)

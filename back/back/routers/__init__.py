from fastapi import APIRouter, Depends
from . import user, community, guest
from core import auth

ROUTER_PREFIX = "/soon/v1"

router = APIRouter(prefix=ROUTER_PREFIX)

router.include_router(guest.router)
router.include_router(user.router, dependencies=[Depends(auth.verify_token)])
router.include_router(community.router, dependencies=[Depends(auth.verify_token)])

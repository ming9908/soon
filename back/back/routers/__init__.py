from fastapi import APIRouter, Depends
from . import post, user, guest, plant
from core import auth

ROUTER_PREFIX = "/soon/v1"

router = APIRouter(prefix=ROUTER_PREFIX)

router.include_router(guest.router)
router.include_router(user.router, dependencies=[Depends(auth.verify_token)])
router.include_router(post.router, dependencies=[Depends(auth.verify_token)])
router.include_router(plant.router, dependencies=[Depends(auth.verify_token)])

"""
피드
- 나의 피드 올리기
- 나의 피드 보기 (식물별로 보기 가능)
- 피드 수정
- 피드 삭제

일정
- 일정 등록
- 일정 수정
- 일정 삭제
- 일정 업데이트 (상태)
- 내 일정 보기 
    -> start, end값을 받아 기간안에있는 모든 일정 리턴

마이페이지
- 회원 수정 (nick, profile)
- 비밀번호 변경
- 공지사항 list 보기

개인정보 처리방침?
Q&A?
알림설정?
"""

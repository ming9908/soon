from fastapi import APIRouter, Depends
from . import post, user, guest, plant, schedule
from core import auth

ROUTER_PREFIX = "/soon/v1"

router = APIRouter(prefix=ROUTER_PREFIX)

router.include_router(guest.router)
router.include_router(user.router, dependencies=[Depends(auth.verify_token)])
router.include_router(post.router, dependencies=[Depends(auth.verify_token)])
router.include_router(plant.router, dependencies=[Depends(auth.verify_token)])
router.include_router(schedule.router, dependencies=[Depends(auth.verify_token)])

"""
피드 (image업로드 이후에 작업가느)
- 나의 피드 올리기
- 나의 피드 보기 (식물별로 보기 가능)
- 피드 수정
- 피드 삭제

게시글
- 삭제처리 확인
- 업데이트 관련 m_id값 들어가는 지 확인

유저
- 삭제 처리 확인
- 업데이트 관련 m_id값 들어가는 지 확인

일정
- 일정 list 보기 (start_date, end_date받아서 기간동안의 일정을 리턴하도록 (datetime값)
    -> status 상관없이 삭제되지 않은 모든 스케쥴은 리턴함

마이페이지
- 회원 수정 (nick, profile)
- 비밀번호 변경
- 공지사항 list 보기

개인정보 처리방침?
Q&A?
알림설정?
"""

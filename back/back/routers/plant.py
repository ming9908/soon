# from services import plant as con
from fastapi import APIRouter


router = APIRouter(tags=["Plant"])


"""
식물 생성
-> 식물 검색 (외부 api 사용)

식물 삭제
식물 죽음 or 살리기
식물 수정(prfile, nick, 물 주기)

식물 리스트

"""

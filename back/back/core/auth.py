import jwt
from fastapi import HTTPException, status
import datetime
from fastapi.security import OAuth2PasswordBearer
from dataclasses import dataclass, asdict

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"

# JWT 토큰을 사용할 때 사용할 OAuth2PasswordBearer 정의
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@dataclass
class Token:
    user_id: str
    nick: str
    exp: datetime.datetime

    def __init__(self, user_id: str, nick: str):
        self.user_id = user_id
        self.nick = nick
        self.exp = datetime.datetime.utcnow() + datetime.timedelta(
            seconds=60 * 60 * 24  # 1일 만료
        )


# JWT 생성 함수
def create_access_token(data: Token):
    encoded_jwt = jwt.encode(asdict(data), SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# JWT 토큰 검증 함수
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


# 토큰을 가져오는 함수
"""def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is invalid",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return username
"""

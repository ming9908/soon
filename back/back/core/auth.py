import jwt
from fastapi import HTTPException, status, Depends
from typing import Optional
import datetime
from fastapi.security import (
    OAuth2PasswordBearer,
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from dataclasses import dataclass, asdict

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"

# JWT 토큰을 사용할 때 사용할 OAuth2PasswordBearer 정의
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@dataclass
class Token:
    user_m_id: str
    user_id: str
    nick: str
    exp: datetime.datetime

    def __init__(self, user_m_id: str, user_id: str, nick: str):
        self.user_m_id = user_m_id
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
def verify_token(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer()),
):
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization token is missing",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        payload = jwt.decode(
            credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM]
        )
        return payload
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

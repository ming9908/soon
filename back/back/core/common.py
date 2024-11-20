from sqids import Sqids
import bcrypt


class Response:
    message: str
    data: any

    def __init__(self, message, data) -> None:
        self.message = message
        self.data = data

    def set_data(self, data):
        self.data = data


# personal code
def make_user_code():
    sqids = Sqids()
    return sqids.encode([1, 2, 3])


def decode_user_code(id):
    sqids = Sqids()
    return sqids.decode(id)


# password hash
def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


# 비밀번호 확인 함수
def verify_password(plain_password: str, hashed_password: str) -> bool:
    # 입력한 비밀번호와 해시된 비밀번호를 비교
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )

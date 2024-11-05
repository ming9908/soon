import datetime
import jwt
import datetime

SECRET_KEY = "secret_key"


class AuthClaims:
    user_id: str
    nick: str
    exp: datetime

    def newClaim(self, id: str, nick: str):
        self.user_id = id
        self.nick = nick
        self.exp = datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60 * 24)


def MakeJWTToken(id: str, nick: str):
    # make token
    claims = AuthClaims.newClaim(id, nick)
    token = jwt.encode(claims, SECRET_KEY, algorithm="HS256")
    return token


def CheckJWTToken(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    return payload

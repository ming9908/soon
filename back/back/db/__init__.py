from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

# 소중한 Secrets.json 가져오기
# from app.config import MONGO_DB_NAME, MONGO_DB_URL

MONGO_DB_URL = "localhost:27017"
MONGO_DB_NAME = "soon"


class MongoDB:
    def __init__(self):
        self.client = None
        self.client = None

    def connect(self):
        self.client = AsyncIOMotorClient(MONGO_DB_URL)
        self.db = self.client[MONGO_DB_NAME]
        print("DB 와 연결되었습니다.")

    def close(self):
        self.client.close()

    def get_collections(self, name: str):
        return self.engine["user"]


mongo = MongoDB()


def mongo_connect():
    mongo.connect()

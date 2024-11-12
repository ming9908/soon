class User:
    __tablename__ = "user"
    username = ""
    nick = ""


async def find_user(self, username):
    # 모델을 만들고 안 만들고는 이부분이 달라질거라 생각된다. engine 을 쓰느냐
    result = await mongodb.engine.find_one(User, User.username == username)
    # print(result)
    # 모델을 만들고 안 만들고는 이부분이 달라질거라 생각된다. client 를 쓰느냐
    # result = await mongodb.client.database 이름.collection 이름.find_one({"username":username})
    if result:
        return result
    else:
        print("거ㅁ색 결과가 없습니다")
    return None


# 회원 찾기
async def find_one(self, username):
    try:
        result = await self.find_user(username)
        if result:
            # result 가 dict 타입일 때와 Model 타입일 때가 문법이 다르므로 적을 때 꼭 살펴보자.
            found_user = dict(
                # result 가 dict
                username=result.username,
                password=result.password,
                # result 가 Model
                # username=result["username"]
                # password=result["password"]
            )
            # 어쨋든 return 은 dict 로 할 거기 때문에 dict 에 넣어준다.
            return found_user
        else:
            print(f"'{username}' 에 대한 검색 결과가 없습니다.")
    except Exception as e:
        print("Error : ", e)
        return e

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/user")
async def postUser():
    return {"message":"user"}

@app.post("login")
async def login():
    return {}

# auth 관련 코드 작성

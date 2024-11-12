from fastapi import FastAPI
import json

from routers import user, community

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(user.router)
app.include_router(community.router)

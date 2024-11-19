from fastapi import FastAPI
from core import auth
import db
import routers

app = FastAPI(
    swagger_ui_parameters={"syntaxHighlight": False}, title="Soon", version="0.0.1"
)

# db connect
db.mongo_connect()

# router
app.include_router(routers.router)

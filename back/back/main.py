from fastapi import FastAPI
from core import auth
import db
import routers

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

# db connect
db.mongo_connect()

# router
app.include_router(routers.router)

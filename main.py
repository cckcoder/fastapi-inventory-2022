from fastapi import FastAPI

from models.database import engine, Base
from models.user import user_model

from routers.inventory import inventory_router
from routers.user import user_router

app = FastAPI()

app.include_router(inventory_router.router)
app.include_router(user_router.router)


@app.get("/")
def hello_world():
    return {"Hello": "World"}


Base.metadata.create_all(engine)
# user_model.Base.metadata.create_all(engine)

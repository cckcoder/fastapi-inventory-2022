from fastapi import FastAPI

from models.database import engine, Base

from routers.inventory import inventory_router

app = FastAPI()

app.include_router(inventory_router.router)


@app.get("/")
def hello_world():
    return {"Hello": "World"}


Base.metadata.create_all(engine)

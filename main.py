from fastapi import FastAPI

from routers.inventory import inventory_router


app = FastAPI()

app.include_router(inventory_router.router)


@app.get("/")
def hello_world():
    return {"Hello": "World"}

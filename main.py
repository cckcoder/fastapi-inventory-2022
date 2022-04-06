from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from models.database import engine, Base
from models.user import user_model

from routers.inventory import inventory_router
from routers.user import user_router
from routers.authen import authen_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authen_router.router)
app.include_router(inventory_router.router)
app.include_router(user_router.router)


@app.get("/")
def hello_world():
    return {"Hello": "World"}


Base.metadata.create_all(engine)
# user_model.Base.metadata.create_all(engine)


app.mount("/static", StaticFiles(directory="static"), name="static")

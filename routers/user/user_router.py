from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy.orm.session import Session

from routers.user import user_controller
from models.user.user_scheme import UserDisplayBase, UserBase
from models.database import get_db

from utils.oauth2 import access_user_token

router = APIRouter(prefix="/user", tags=["user"])


@router.get(
    "/", response_model=List[UserDisplayBase], dependencies=[Depends(access_user_token)]
)
async def all_user(db: Session = Depends(get_db)):
    return await user_controller.get_all_user(db)


@router.get(
    "/{user_id}",
    response_model=UserDisplayBase,
    dependencies=[Depends(access_user_token)],
)
async def user_by_id(user_id: int, db: Session = Depends(get_db)):
    return await user_controller.get_user_by_id(db, user_id)


@router.post("/", response_model=UserDisplayBase)
async def register_user(request: UserBase, db: Session = Depends(get_db)):
    return await user_controller.create_user(db, request)


@router.put(
    "/{user_id}", response_model=UserBase, dependencies=[Depends(access_user_token)]
)
async def updated_user(user_id: int, request: UserBase, db: Session = Depends(get_db)):
    return await user_controller.update_user(db, user_id, request)


@router.delete("/{user_id}", dependencies=[Depends(access_user_token)])
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return await user_controller.delete_user(db, user_id)

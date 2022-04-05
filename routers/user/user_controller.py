from pprint import pprint
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from utils.hash import Hash
from models.user.user_scheme import UserBase
from models.user.user_model import DbUser


async def create_user(db: Session, request: UserBase):
    new_user = DbUser(username=request.username, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_user(db: Session, user_id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == user_id)
    if user.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with {user_id} not found",
        )
    else:
        user.update(
            {
                DbUser.username: request.username,
                DbUser.password: Hash.bcrypt(request.password),
            }
        )
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"detail": f"user id {user_id} updated successfully"},
        )


async def get_all_user(db: Session):
    return db.query(DbUser).order_by(DbUser.created_date.desc()).all()


async def get_user_by_id(db: Session, user_id: int):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user id: {user_id} not found",
        )
    return user


async def delete_user(db: Session, user_id: int):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user id: {user_id} not found",
        )
    else:
        db.delete(user)
        db.commit()
        return JSONResponse(
            content={"detail": f"user id {user_id} deleted successfully"},
            status_code=status.HTTP_200_OK,
        )

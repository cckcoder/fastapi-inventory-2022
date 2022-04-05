from typing import Optional
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

from sqlalchemy.orm.session import Session
from models.database import get_db
from models.user import user_model

from jose import jwt
from jose import JWSError

from decouple import config

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def create_access_token(data: dict, expire_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = await generate_expire_date(expire_delta)

    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


async def access_user_token(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise await create_access_token()
    except JWSError:
        raise await create_access_token()


async def generate_expire_date(expire_delta: Optional[timedelta] = None):
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(days=1)
    return expire


async def credentials_exception():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

from pprint import pprint
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm. session import Session
from models.database import get_db


router = APIRouter(tags=["authentication"])


@router.post("/login")
async def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    print("**********")
    pprint(request.username)
    pprint(request.password)
    print("**********")
    return { "Hello": "Authentication"}
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str


class UserDisplayBase(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

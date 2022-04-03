from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel


class InventoryBase(BaseModel):
    description: str
    image_name: str
    price: Decimal
    stock: int

    # class Config:
    #     orm_mode = True


class InventoryDisplayBase(BaseModel):
    id: int
    description: str
    image_name: str
    price: Decimal
    stock: int
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True

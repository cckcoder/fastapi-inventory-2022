from decimal import Decimal
from pydantic import BaseModel


class InventoryBase(BaseModel):
    description: str
    image_name: str
    price: Decimal
    stock: int

    class Config:
        orm_mode = True

from fastapi import status

from sqlalchemy.orm import Session

from models.inventory.inventory_model import DbInventory
from models.inventory.inventory_scheme import InventoryBase


async def create_inventory(db: Session, requset: InventoryBase):
    new_inventory = DbInventory(
        description=requset.description,
        image_name=requset.image_name,
        price=requset.price,
        stock=requset.stock,
    )

    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory


async def get_all_inventory(db: Session):
    inventory = db.query(DbInventory).order_by(DbInventory.description.desc()).all()
    return inventory

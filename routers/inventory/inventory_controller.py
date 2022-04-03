from pprint import pprint
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

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


async def inventory_by_id(db: Session, inventory_id: int):
    inventory = db.query(DbInventory).filter(DbInventory.id == inventory_id).first()
    return inventory


async def deleted_inventory(db: Session, inventory_id: int):
    inventory = db.query(DbInventory).filter(DbInventory.id == inventory_id).first()
    if inventory is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Inventory with id {inventory_id} not found",
        )
    else:
        db.delete(inventory)
        db.commit()
        return JSONResponse(
            content={
                "detail": f"Inventory with id {inventory_id} deleted successfully"
            },
            status_code=status.HTTP_200_OK,
        )


async def update_inventory(db: Session, inventory_id: int, request: InventoryBase):
    inventory = db.query(DbInventory).filter(DbInventory.id == inventory_id).first()
    inventory.description=request.description
    inventory.image_name=request.image_name
    inventory.price=request.price
    inventory.stock=request.stock
    db.commit()
    db.refresh(inventory)
    return inventory

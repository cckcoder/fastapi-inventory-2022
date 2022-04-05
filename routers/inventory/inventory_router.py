from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy.orm import Session

from models.inventory.inventory_scheme import InventoryBase, InventoryDisplayBase
from models.database import get_db
from routers.inventory import inventory_controller
from utils.oauth2 import access_user_token

router = APIRouter(prefix="/inventory", tags=["inventory"], dependencies=[Depends(access_user_token)])


@router.get("/", response_model=List[InventoryDisplayBase])
async def all_inventory(db: Session = Depends(get_db)):
    return await inventory_controller.get_all_inventory(db)


@router.get("/{inventory_id}", response_model=InventoryDisplayBase)
async def inventory(inventory_id: int, db: Session = Depends(get_db)):
    return await inventory_controller.inventory_by_id(db, inventory_id)


@router.post("/", response_model=InventoryDisplayBase)
async def create_inventory(request: InventoryBase, db: Session = Depends(get_db)):
    return await inventory_controller.create_inventory(db, request)


@router.put("/{inventory_id}", response_model=InventoryDisplayBase)
async def update_inventory(
    inventory_id: int, request: InventoryBase, db: Session = Depends(get_db)
):
    return await inventory_controller.update_inventory(db, inventory_id, request)


@router.delete("/{inventory_id}")
async def delete_inventory(inventory_id: int, db: Session = Depends(get_db)):
    return await inventory_controller.deleted_inventory(db, inventory_id)

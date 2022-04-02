from pprint import pprint
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from models.inventory.inventory_scheme import InventoryBase
from models.database import get_db
from routers.inventory import inventory_controller

router = APIRouter(prefix="/inventory", tags=["inventory"])


@router.get("/")
async def all_inventory():
    return {"msg": "all_inventory"}


@router.get("/{inventory_id}")
async def inventory(inventory_id: int):
    return {"msg": f"inventory id: {inventory_id}"}


@router.post("/", response_model=InventoryBase)
async def create_inventory(request: InventoryBase, db: Session = Depends(get_db)):
    pprint(request)
    return await inventory_controller.create_inventory(db, request)


@router.put("/{inventory_id}")
async def update_inventory(inventory_id: int):
    return {"msg": f"update id: {inventory_id}"}


@router.delete("/{inventory_id}")
async def delete_inventory(inventory_id: int):
    return {"msg": f"delete id: {inventory_id}"}

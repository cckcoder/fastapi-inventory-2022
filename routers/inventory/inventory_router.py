from fastapi import APIRouter

router = APIRouter(prefix="/inventory", tags=["inventory"])


@router.get("/")
async def all_inventory():
    return {"msg": "all_inventory"}


@router.get("/{inventory_id}")
async def inventory(inventory_id: int):
    return {"msg": f"inventory id: {inventory_id}"}


@router.post("/")
async def create_inventory():
    return {"msg": f"create inventory"}


@router.put("/{inventory_id}")
async def update_inventory(inventory_id: int):
    return {"msg": f"update id: {inventory_id}"}


@router.delete("/{inventory_id}")
async def delete_inventory(inventory_id: int):
    return {"msg": f"delete id: {inventory_id}"}

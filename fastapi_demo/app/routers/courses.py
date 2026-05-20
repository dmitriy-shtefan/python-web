from fastapi import APIRouter


router = APIRouter()


@router.get("/my_route")
async def my_route():
    return {"hello": "world"}


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
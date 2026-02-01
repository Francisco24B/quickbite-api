from fastapi import APIRouter


router = APIRouter(prefix="/orders", tags=["orders"])

orders = []


@router.post("/")
def create_order(order: dict):
    orders.append(order)
    return {"message": "Order created", "order": order}


@router.get("/")
def list_orders():
    return orders

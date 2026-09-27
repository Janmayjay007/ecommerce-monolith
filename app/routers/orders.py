from fastapi import APIRouter

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/ping")
def ping():
    return {"router": "orders", "status": "alive"}


# TODO (Phase 3): implement POST /orders/checkout (cart -> order,
# clear cart) and GET /orders (order history for current user).

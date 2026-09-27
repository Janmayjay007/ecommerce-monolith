from fastapi import APIRouter

router = APIRouter(prefix="/cart", tags=["cart"])


@router.get("/ping")
def ping():
    return {"router": "cart", "status": "alive"}


# TODO (Phase 3): implement add/remove/view cart endpoints,
# backed by Redis (session-based) or the database.

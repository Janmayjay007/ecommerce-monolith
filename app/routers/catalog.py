from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["catalog"])


@router.get("/ping")
def ping():
    return {"router": "catalog", "status": "alive"}


# TODO (Phase 3): implement GET /products (list/search) and
# GET /products/{id} using database.get_db and schemas.ProductRead.

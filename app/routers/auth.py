from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/ping")
def ping():
    return {"router": "auth", "status": "alive"}


# TODO (Phase 2): implement /signup and /login using database.get_db,
# password hashing (passlib), and JWT token creation.

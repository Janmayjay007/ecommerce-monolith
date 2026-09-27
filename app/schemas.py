from datetime import datetime

from pydantic import BaseModel, EmailStr


# ---- Users ----
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserRead(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


# ---- Products ----
class ProductRead(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    image_url: str | None = None

    class Config:
        from_attributes = True


# ---- Cart ----
class CartItemAdd(BaseModel):
    product_id: int
    quantity: int = 1


# ---- Orders ----
class OrderRead(BaseModel):
    id: int
    total_amount: float
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

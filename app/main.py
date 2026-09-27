from fastapi import FastAPI

from app.routers import auth, cart, catalog, orders

app = FastAPI(title="E-commerce Monolith")

app.include_router(auth.router)
app.include_router(catalog.router)
app.include_router(cart.router)
app.include_router(orders.router)


@app.get("/")
def read_root():
    return {"status": "ok", "message": "E-commerce API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}

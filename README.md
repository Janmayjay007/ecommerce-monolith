# E-commerce Monolith (FastAPI)

Phase 0 scaffold — project structure with placeholder routers for
auth, catalog, cart, and orders. Nothing is implemented yet beyond
`/ping` health checks per router; this just proves the app runs and
is organized correctly before adding real logic.

## Run it locally

```bash
docker compose up --build
```

Then open:
- http://localhost:8000/ — root health check
- http://localhost:8000/docs — interactive API docs (Swagger UI)
- http://localhost:8000/auth/ping, /products/ping, /cart/ping, /orders/ping — router checks

Postgres runs on `localhost:5432` (user/pass: `postgres`/`postgres`,
db: `ecommerce`) and Redis on `localhost:6379`, both from the
`docker-compose.yml` services — no separate install needed.

## Run without Docker (optional)

```bash
python3 -m venv venv
source venv/bin/activate       # on Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Note: this requires your own local Postgres/Redis, or edit
`DATABASE_URL` in `.env` to point elsewhere.

## Project structure

```
app/
├── main.py          # app entrypoint, includes all routers
├── database.py      # SQLAlchemy engine/session setup
├── models.py         # DB tables: User, Product, Order, OrderItem
├── schemas.py        # Pydantic request/response shapes
├── dependencies.py   # shared logic (e.g. get_current_user later)
└── routers/
    ├── auth.py        # signup/login (Phase 2)
    ├── catalog.py      # product listing (Phase 3)
    ├── cart.py          # cart add/remove/view (Phase 3)
    └── orders.py        # checkout/order history (Phase 3)
```

## Next steps
See the project roadmap — Phase 1 (database) and Phase 2 (auth) are next.

from fastapi import FastAPI, APIRouter

app = FastAPI()

# --- Users Router ---
users_router = APIRouter(prefix="/users", tags=["Users"])

@users_router.get("/")
def list_users():
    return [{"id": 1, "name": "Ajay"}, {"id": 2, "name": "Ravi"}]

@users_router.get("/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# --- Products Router ---
products_router = APIRouter(prefix="/products", tags=["Products"])

@products_router.get("/")
def list_products():
    return [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Phone"}]

@products_router.post("/")
def add_product(name: str):
    return {"added": name}

# Register routers with main app
app.include_router(users_router)
app.include_router(products_router)

# Run: uvicorn routing:app --reload

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routers import user_router

app = FastAPI(
    # title="FastAPI Minimal User App",
    # version="1.0.0",
    # description="FastAPI project with user CRUD only"
)

# Create DB tables if not exist
Base.metadata.create_all(bind=engine)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Allow all in dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.router, prefix="/api/v1/auth", tags=["Auth"])

# Root route
@app.get("/")
def root():
    return {"message": "User CRUD FastAPI running"}

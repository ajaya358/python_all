from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from sqlalchemy import text
from contextlib import asynccontextmanager
from app.db.db import login_engine, product_engine, Base
from app.models import user, product
from app.api.v1.api import router
from app.core.limiter import limiter
from app.core.exceptions import NotFoundException, BadRequestException, UnauthorizedException
from app.core.exception_handlers import (
    not_found_exception_handler,
    bad_request_exception_handler,
    unauthorized_exception_handler,
    validation_exception_handler,
    general_exception_handler
)
from dotenv import load_dotenv
import logging
import os

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        with login_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            logger.info("✅ LoginDB connected!")
    except Exception as e:
        logger.error(f"❌ LoginDB failed: {e}")

    try:
        with product_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            logger.info("✅ ProductDB connected!")
    except Exception as e:
        logger.error(f"❌ ProductDB failed: {e}")

    Base.metadata.create_all(bind=login_engine)
    logger.info("✅ LoginDB tables created!")

    Base.metadata.create_all(bind=product_engine)
    logger.info("✅ ProductDB tables created!")

    yield

app = FastAPI(
    title="My FastAPI App",
    description="Learning FastAPI step by step",
    version="1.0.0",
    lifespan=lifespan
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# ── Exception Handlers ─────────────────────────
app.add_exception_handler(NotFoundException, not_found_exception_handler)
app.add_exception_handler(BadRequestException, bad_request_exception_handler)
app.add_exception_handler(UnauthorizedException, unauthorized_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

# ── CORS ───────────────────────────────────────
allowed_origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()

# ── DB Config from .env ────────────────────────
DB_HOST     = os.getenv("DB_HOST")
DB_USER     = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_OPTIONS  = os.getenv("DB_OPTIONS")

LOGIN_DB_NAME   = os.getenv("LOGIN_DB_NAME")
PRODUCT_DB_NAME = os.getenv("PRODUCT_DB_NAME")

# ── Build URLs (like MongoDB style) ───────────
def build_url(db_name):
    return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{db_name}?{DB_OPTIONS}"

LOGIN_DB_URL   = build_url(LOGIN_DB_NAME)
PRODUCT_DB_URL = build_url(PRODUCT_DB_NAME)

# ── Engines ────────────────────────────────────
login_engine   = create_engine(LOGIN_DB_URL)
product_engine = create_engine(PRODUCT_DB_URL)

# ── Sessions ───────────────────────────────────
LoginSession   = sessionmaker(autocommit=False, autoflush=False, bind=login_engine)
ProductSession = sessionmaker(autocommit=False, autoflush=False, bind=product_engine)

# ── Base for ORM models ────────────────────────
class Base(DeclarativeBase):
    pass

# ── DB Dependencies ────────────────────────────
def get_login_db():
    db = LoginSession()
    try:
        yield db
    finally:
        db.close()

def get_product_db():
    db = ProductSession()
    try:
        yield db
    finally:
        db.close()

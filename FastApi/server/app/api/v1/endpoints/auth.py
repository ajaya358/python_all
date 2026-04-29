from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.db import get_login_db
from app.schemas.auth import TokenResponse
from app.services import auth_service
from app.core.limiter import limiter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse)
@limiter.limit("5/minute")
def login(request: Request, form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_login_db)):
    return auth_service.login(db, email=form.username, password=form.password)

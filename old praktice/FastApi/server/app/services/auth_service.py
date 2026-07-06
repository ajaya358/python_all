from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.utils.hashing import verify_password
from app.utils.jwt import create_access_token
from app.core.exceptions import UnauthorizedException
import logging

logger = logging.getLogger(__name__)

def login(db: Session, email: str, password: str):
    logger.info(f"Login attempt for email: {email}")
    user = db.query(User).filter(User.email == email).first()
    if not user:
        logger.warning(f"User not found: {email}")
        raise UnauthorizedException("Invalid email or password")
    if not verify_password(password, user.password):
        logger.warning(f"Wrong password for: {email}")
        raise UnauthorizedException("Invalid email or password")
    token = create_access_token(data={"sub": user.email, "user_id": user.id})
    logger.info(f"Login successful for: {email}")
    return {"access_token": token, "token_type": "bearer"}

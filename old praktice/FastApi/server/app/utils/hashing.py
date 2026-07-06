import bcrypt
import logging

logger = logging.getLogger(__name__)

def hash_password(password: str) -> str:
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    logger.info("Password hashed successfully")
    return hashed.decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        hashed_bytes = hashed_password.strip().encode("utf-8")
        result = bcrypt.checkpw(plain_password.encode("utf-8"), hashed_bytes)
        logger.info(f"Password verification result: {result}")
        return result
    except Exception as e:
        logger.error(f"Password verification error: {e}")
        return False

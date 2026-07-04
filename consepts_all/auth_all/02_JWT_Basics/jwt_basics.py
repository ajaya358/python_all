# JWT Basics - Create, sign, and verify tokens
# pip install python-jose[cryptography]

from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key-keep-it-safe"  # use long random string in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# --- Create JWT Token ---
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# --- Verify JWT Token ---
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            return None
        return payload
    except JWTError:
        return None

# --- Demo ---
print("=== Creating Token ===")
token = create_access_token(data={"sub": "1", "email": "ajay@email.com", "role": "user"})
print(f"Token: {token[:50]}...")

print("\n=== Verifying Token ===")
payload = verify_token(token)
if payload:
    print(f"Valid! User ID: {payload['sub']}, Email: {payload['email']}")
else:
    print("Invalid or expired token")

print("\n=== Verifying Fake Token ===")
result = verify_token("fake.token.here")
print("Result:", result)  # None

print("\n=== Token Payload Contains ===")
import json, base64
parts = token.split(".")
padded = parts[1] + "=" * (4 - len(parts[1]) % 4)
decoded = json.loads(base64.b64decode(padded))
print(decoded)

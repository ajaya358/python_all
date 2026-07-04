# OAuth2 + JWT Auth in FastAPI - Complete Login System
# pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt] python-multipart

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timedelta

SECRET_KEY = "supersecretkey123changethisinproduction"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# --- Fake DB ---
fake_users_db = {
    "ajay@email.com": {
        "id": 1,
        "name": "Ajay",
        "email": "ajay@email.com",
        "hashed_password": pwd_context.hash("password123"),
        "role": "user",
    }
}

# --- Schemas ---
class Token(BaseModel):
    access_token: str
    token_type: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    role: str

# --- Helpers ---
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_token(data: dict):
    data.update({"exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email or email not in fake_users_db:
            raise HTTPException(status_code=401, detail="Invalid token")
        return fake_users_db[email]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# --- Routes ---
@app.post("/login", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form.username)
    if not user or not verify_password(form.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token({"sub": user["email"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/me", response_model=UserOut)
def get_me(current_user=Depends(get_current_user)):
    return current_user

@app.get("/protected")
def protected_route(current_user=Depends(get_current_user)):
    return {"message": f"Hello {current_user['name']}, you are authenticated!"}

# Run: uvicorn oauth2_fastapi:app --reload
# Test: POST /login with form data: username=ajay@email.com, password=password123
# Then use token in: GET /me  with Authorization: Bearer <token>

# Role Based Access Control (RBAC) in FastAPI
# Different users have different permissions: admin, user, moderator

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

SECRET_KEY = "supersecretkey123"
ALGORITHM = "HS256"

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# --- Get current user from token ---
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"id": payload.get("sub"), "role": payload.get("role")}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# --- Role checker dependency ---
def require_role(*roles):
    def checker(current_user=Depends(get_current_user)):
        if current_user["role"] not in roles:
            raise HTTPException(
                status_code=403,
                detail=f"Access denied. Required roles: {list(roles)}"
            )
        return current_user
    return checker

# --- Routes with role protection ---
@app.get("/user/dashboard")
def user_dashboard(user=Depends(require_role("user", "admin"))):
    return {"message": f"Welcome user {user['id']}"}

@app.get("/admin/dashboard")
def admin_dashboard(user=Depends(require_role("admin"))):
    return {"message": "Admin panel — full access"}

@app.delete("/admin/delete/{item_id}")
def delete_item(item_id: int, user=Depends(require_role("admin"))):
    return {"deleted": item_id, "by": user["id"]}

@app.get("/moderator/reports")
def view_reports(user=Depends(require_role("admin", "moderator"))):
    return {"reports": ["report1", "report2"]}

# --- Role summary ---
print("=== Roles ===")
roles = {
    "user":      "Can view own data, use basic features",
    "moderator": "Can view reports, manage content",
    "admin":     "Full access — create, update, delete everything",
}
for role, perm in roles.items():
    print(f"  {role:12}: {perm}")

# Run: uvicorn role_based_access:app --reload

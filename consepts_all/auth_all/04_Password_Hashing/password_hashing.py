# Password Hashing - Never store plain text passwords
# pip install passlib[bcrypt]

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- Hash a password ---
def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)

# --- Verify password against hash ---
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# --- Demo ---
print("=== Password Hashing ===")
password = "MySecret@123"
hashed = hash_password(password)
print(f"Plain:  {password}")
print(f"Hashed: {hashed}")

print("\n=== Verify Password ===")
print("Correct password:", verify_password("MySecret@123", hashed))   # True
print("Wrong password:  ", verify_password("wrongpassword", hashed))  # False

print("\n=== Why Hashing? ===")
reasons = [
    "Even if DB is hacked, passwords are safe",
    "bcrypt is slow by design — hard to brute force",
    "Same password hashes differently each time (salt)",
    "Cannot reverse hash back to original password",
]
for r in reasons:
    print(f"  - {r}")

print("\n=== Same password, different hash each time ===")
h1 = hash_password("test123")
h2 = hash_password("test123")
print(f"Hash 1: {h1[:30]}...")
print(f"Hash 2: {h2[:30]}...")
print(f"Same?   {h1 == h2}")  # False — bcrypt adds random salt
print(f"Verify: {verify_password('test123', h1)}")  # True

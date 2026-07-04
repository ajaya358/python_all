# Authentication & Authorization - Introduction
# Auth = Who are you? (Authentication) + What can you do? (Authorization)

print("=== Key Concepts ===")
concepts = {
    "Authentication": "Verify identity — login with username/password",
    "Authorization":  "Verify permissions — can this user access this resource?",
    "JWT":            "JSON Web Token — stateless token sent with every request",
    "OAuth2":         "Standard protocol for token-based auth (used by Google, GitHub)",
    "Bearer Token":   "Token sent in Authorization header: Bearer <token>",
    "Hashing":        "One-way encryption of passwords (bcrypt)",
    "Salt":           "Random data added before hashing to prevent rainbow attacks",
    "Access Token":   "Short-lived token (15 min) for API access",
    "Refresh Token":  "Long-lived token (7 days) to get new access token",
    "RBAC":           "Role Based Access Control — admin, user, moderator roles",
}
for k, v in concepts.items():
    print(f"  {k:18}: {v}")

print("\n=== JWT Structure ===")
print("  JWT = Header.Payload.Signature")
print("  Header:    algorithm used (HS256)")
print("  Payload:   user data (id, email, role, expiry)")
print("  Signature: verifies token not tampered")
print()
print("  Example token:")
print("  eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIn0.abc123xyz")

print("\n=== Auth Flow ===")
flow = [
    "1. User sends POST /login with email + password",
    "2. Server checks password hash matches DB",
    "3. Server creates JWT token with user_id + expiry",
    "4. Server returns token to client",
    "5. Client stores token (localStorage / cookie)",
    "6. Client sends token in every request: Authorization: Bearer <token>",
    "7. Server verifies token on each protected route",
    "8. If valid → allow, if expired/invalid → 401 Unauthorized",
]
for step in flow:
    print(f"  {step}")

print("\n=== Install ===")
print("  pip install python-jose[cryptography] passlib[bcrypt] python-multipart")

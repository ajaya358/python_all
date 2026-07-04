# Rate Limiting - Prevent API abuse and DDoS attacks
# pip install fastapi slowapi

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from collections import defaultdict
import time

app = FastAPI()

# --- Simple in-memory rate limiter (for learning) ---
request_counts = defaultdict(list)

def is_rate_limited(client_ip: str, max_requests: int = 10, window_seconds: int = 60) -> bool:
    now = time.time()
    # Remove old requests outside the window
    request_counts[client_ip] = [
        t for t in request_counts[client_ip] if now - t < window_seconds
    ]
    if len(request_counts[client_ip]) >= max_requests:
        return True
    request_counts[client_ip].append(now)
    return False

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host
    if is_rate_limited(client_ip, max_requests=10, window_seconds=60):
        return JSONResponse(
            status_code=429,
            content={"error": "Too many requests. Try again later."}
        )
    return await call_next(request)

@app.get("/")
def root():
    return {"message": "OK"}

# --- Production: use slowapi (Redis-backed) ---
print("=== Production Rate Limiting with slowapi ===")
print("""
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/search")
@limiter.limit("5/minute")          # 5 requests per minute per IP
def search(request: Request, q: str):
    return {"results": []}

@app.post("/login")
@limiter.limit("3/minute")          # 3 login attempts per minute
def login(request: Request):
    return {"token": "..."}

@app.get("/public")
@limiter.limit("100/minute")        # generous limit for public endpoints
def public(request: Request):
    return {"data": []}
""")

print("=== Rate Limit Strategies ===")
strategies = {
    "Per IP":       "Limit by client IP address",
    "Per User":     "Limit by authenticated user ID",
    "Per API Key":  "Limit by API key (for B2B APIs)",
    "Global":       "Total requests across all clients",
}
for k, v in strategies.items():
    print(f"  {k:12}: {v}")

# Run: uvicorn rate_limiting:app --reload

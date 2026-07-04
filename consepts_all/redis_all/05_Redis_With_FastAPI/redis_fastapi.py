# Redis + FastAPI - Caching, Sessions, Rate Limiting
# pip install fastapi uvicorn redis
# Start Redis: docker run -d -p 6379:6379 redis

from fastapi import FastAPI, HTTPException, Request, Depends
import redis
import json
import time
import hashlib

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# --- 1. Response Caching ---
def get_cache(key: str):
    data = r.get(key)
    return json.loads(data) if data else None

def set_cache(key: str, value, ttl: int = 300):
    r.set(key, json.dumps(value), ex=ttl)

@app.get("/products")
def get_products(category: str = "all"):
    cache_key = f"products:{category}"
    cached = get_cache(cache_key)
    if cached:
        return {"source": "cache", "data": cached}

    # Simulate DB query
    time.sleep(0.1)
    products = [{"id": 1, "name": "Laptop", "category": category}]
    set_cache(cache_key, products, ttl=60)
    return {"source": "db", "data": products}

@app.delete("/products/cache")
def clear_product_cache():
    keys = r.keys("products:*")
    if keys:
        r.delete(*keys)
    return {"cleared": len(keys)}

# --- 2. Session Storage ---
@app.post("/login")
def login(username: str, password: str):
    if username == "ajay" and password == "pass123":
        session_id = hashlib.sha256(f"{username}{time.time()}".encode()).hexdigest()
        r.hset(f"session:{session_id}", mapping={"user": username, "role": "admin"})
        r.expire(f"session:{session_id}", 3600)  # 1 hour
        return {"session_id": session_id}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/profile")
def get_profile(session_id: str):
    session = r.hgetall(f"session:{session_id}")
    if not session:
        raise HTTPException(status_code=401, detail="Session expired or invalid")
    return {"user": session["user"], "role": session["role"]}

@app.post("/logout")
def logout(session_id: str):
    r.delete(f"session:{session_id}")
    return {"message": "Logged out"}

# --- 3. Rate Limiting ---
@app.get("/api/data")
def get_data(request: Request):
    ip = request.client.host
    key = f"rate:{ip}"
    count = r.incr(key)
    if count == 1:
        r.expire(key, 60)  # reset every 60 seconds
    if count > 10:
        raise HTTPException(status_code=429, detail="Too many requests")
    return {"data": "some data", "requests_used": count}

# Run: uvicorn redis_fastapi:app --reload

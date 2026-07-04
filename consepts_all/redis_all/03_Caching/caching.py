# Redis Caching - Speed up your app by caching expensive operations
# pip install redis

import redis
import json
import time
import functools

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# --- Cache-Aside Pattern (most common) ---
def get_user(user_id: int):
    cache_key = f"user:{user_id}"

    # 1. Check cache first
    cached = r.get(cache_key)
    if cached:
        print(f"  [CACHE HIT] user:{user_id}")
        return json.loads(cached)

    # 2. Cache miss — fetch from DB
    print(f"  [CACHE MISS] Fetching user:{user_id} from DB...")
    time.sleep(0.1)  # simulate DB query
    user = {"id": user_id, "name": "Ajay", "email": "ajay@email.com"}

    # 3. Store in cache with TTL
    r.set(cache_key, json.dumps(user), ex=300)  # cache for 5 minutes
    return user

print("=== Cache-Aside Pattern ===")
print("First call (DB):", get_user(1))
print("Second call (cache):", get_user(1))

# --- Cache Decorator ---
def cache(ttl=300):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = f"cache:{func.__name__}:{args}:{kwargs}"
            cached = r.get(key)
            if cached:
                return json.loads(cached)
            result = func(*args, **kwargs)
            r.set(key, json.dumps(result), ex=ttl)
            return result
        return wrapper
    return decorator

@cache(ttl=60)
def get_products(category: str):
    time.sleep(0.2)  # simulate slow DB query
    return [{"id": 1, "name": "Laptop", "category": category}]

print("\n=== Cache Decorator ===")
print(get_products("electronics"))
print(get_products("electronics"))  # from cache

# --- Cache Invalidation ---
def update_user(user_id: int, name: str):
    # Update DB...
    # Delete cache so next read gets fresh data
    r.delete(f"user:{user_id}")
    print(f"  Cache invalidated for user:{user_id}")

print("\n=== Cache Invalidation ===")
update_user(1)

# --- Caching Patterns Summary ---
print("\n=== Caching Patterns ===")
patterns = {
    "Cache-Aside":   "App checks cache, on miss fetches DB and stores in cache",
    "Write-Through": "Write to cache AND DB at same time",
    "Write-Behind":  "Write to cache first, async write to DB later",
    "Read-Through":  "Cache fetches from DB automatically on miss",
}
for k, v in patterns.items():
    print(f"  {k:16}: {v}")

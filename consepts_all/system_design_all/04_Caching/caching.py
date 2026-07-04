# Caching - Store frequently accessed data for fast retrieval

print("=== What is Caching? ===")
print("  Store results of expensive operations temporarily")
print("  Next request gets data from cache instead of DB/API\n")

print("=== Cache Hit vs Miss ===")
print("  Cache HIT:  Data found in cache → return instantly (< 1ms)")
print("  Cache MISS: Data not in cache → fetch from DB → store in cache\n")

print("=== Caching Layers ===")
layers = {
    "Browser Cache":    "Static files cached in user browser (CSS, JS, images)",
    "CDN":              "Cache static + dynamic content close to users globally",
    "API Gateway":      "Cache API responses at gateway level",
    "Application":      "Redis/Memcached — cache DB queries, computed results",
    "Database":         "DB query cache, buffer pool",
}
for k, v in layers.items():
    print(f"  {k:18}: {v}")

print("\n=== Cache Eviction Policies ===")
policies = {
    "LRU (Least Recently Used)":    "Remove item not accessed for longest time",
    "LFU (Least Frequently Used)":  "Remove item accessed fewest times",
    "FIFO (First In First Out)":    "Remove oldest item",
    "TTL (Time To Live)":           "Remove item after fixed time",
    "Random":                       "Remove random item",
}
for k, v in policies.items():
    print(f"  {k:35}: {v}")

print("\n=== Cache Invalidation Strategies ===")
strategies = {
    "TTL":              "Auto-expire after N seconds — simple but stale data possible",
    "Write-Through":    "Update cache when DB is updated — always fresh",
    "Write-Behind":     "Update cache first, DB later async — fast writes",
    "Cache-Aside":      "App manages cache manually — most flexible",
    "Event-Based":      "Invalidate cache when event published (Kafka/Redis Pub/Sub)",
}
for k, v in strategies.items():
    print(f"  {k:18}: {v}")

print("\n=== What to Cache ===")
good = [
    "DB query results that don't change often (product catalog)",
    "User profile data",
    "API responses from third-party services",
    "Computed/aggregated results (total sales, leaderboard)",
    "Session data",
    "HTML fragments",
]
print("  Good to cache:")
for g in good:
    print(f"    - {g}")

bad = [
    "Frequently changing data (stock prices — use short TTL)",
    "User-specific sensitive data (be careful with TTL)",
    "Large objects (watch memory usage)",
]
print("  Be careful caching:")
for b in bad:
    print(f"    - {b}")

print("\n=== LRU Cache Implementation ===")
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

cache = LRUCache(3)
cache.put("user:1", {"name": "Ajay"})
cache.put("user:2", {"name": "Ravi"})
cache.put("user:3", {"name": "Priya"})
cache.put("user:4", {"name": "Kumar"})  # evicts user:1
print("user:1:", cache.get("user:1"))   # None (evicted)
print("user:2:", cache.get("user:2"))   # found

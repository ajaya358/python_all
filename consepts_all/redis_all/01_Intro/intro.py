# Redis - In-Memory Data Store
# pip install redis
# Start: docker run -d -p 6379:6379 redis

print("=== What is Redis? ===")
concepts = {
    "Redis":          "In-memory key-value store — extremely fast (microseconds)",
    "In-Memory":      "Data stored in RAM, not disk — very fast but limited size",
    "Key-Value":      "Store any value with a unique key",
    "TTL":            "Time To Live — auto-expire keys after N seconds",
    "Persistence":    "RDB (snapshots) or AOF (append-only log) to save to disk",
    "Pub/Sub":        "Publish/Subscribe messaging pattern",
    "Atomic":         "All Redis operations are atomic — thread safe",
}
for k, v in concepts.items():
    print(f"  {k:14}: {v}")

print("\n=== Redis Data Types ===")
data_types = {
    "String":   "Simple text/number — SET name 'Ajay'",
    "List":     "Ordered list — push/pop from both ends",
    "Hash":     "Dictionary — store object fields",
    "Set":      "Unique unordered values",
    "Sorted Set":"Unique values with score — leaderboards",
    "Stream":   "Append-only log — like Kafka lite",
}
for k, v in data_types.items():
    print(f"  {k:12}: {v}")

print("\n=== Common Use Cases ===")
use_cases = [
    "Caching — store DB query results, API responses",
    "Session storage — store user sessions",
    "Rate limiting — count requests per IP",
    "Leaderboards — sorted sets for rankings",
    "Pub/Sub — real-time notifications",
    "Job queues — Celery uses Redis as broker",
    "Distributed locks — prevent race conditions",
]
for u in use_cases:
    print(f"  - {u}")

print("\n=== Install & Connect ===")
print("  pip install redis")
print("  docker run -d -p 6379:6379 --name redis redis")
print("  redis-cli ping  →  PONG")

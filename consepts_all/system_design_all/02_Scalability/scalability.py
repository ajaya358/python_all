# Scalability - Handle growing traffic and data

print("=== Scalability Strategies ===")

print("\n1. Horizontal Scaling (most important)")
print("""
  Add more servers behind a load balancer
  
  [Client] → [Load Balancer] → [Server 1]
                             → [Server 2]
                             → [Server 3]
  
  - Stateless servers (no session stored on server)
  - Sessions stored in Redis (shared across servers)
  - Easy to add/remove servers
""")

print("2. Database Scaling")
db_scaling = {
    "Read Replicas":    "One master (writes) + multiple replicas (reads)",
    "Sharding":         "Split data across multiple DBs by user_id, region, etc.",
    "Connection Pool":  "Reuse DB connections instead of creating new ones",
    "Query Optimization":"Indexes, avoid N+1, use EXPLAIN",
}
for k, v in db_scaling.items():
    print(f"  {k:20}: {v}")

print("\n3. Caching Layers")
cache_layers = {
    "CDN":          "Cache static files (images, JS, CSS) close to users",
    "API Cache":    "Cache API responses in Redis",
    "DB Cache":     "Cache DB query results",
    "Browser":      "Cache in user's browser (Cache-Control headers)",
}
for k, v in cache_layers.items():
    print(f"  {k:14}: {v}")

print("\n4. Async Processing")
print("""
  Instead of doing everything in the request:
  - Heavy tasks → Celery/Kafka queue → background worker
  - User gets instant response
  - Worker processes in background
  
  Example: User uploads image
  ❌ Slow: resize image → save → respond (5 seconds)
  ✅ Fast: save original → respond instantly → worker resizes async
""")

print("5. Microservices")
print("  Split monolith into services → scale only what needs scaling")
print("  Example: Scale only the search service during peak search traffic\n")

print("=== Numbers Every Developer Should Know ===")
numbers = {
    "L1 cache":         "0.5 ns",
    "RAM access":       "100 ns",
    "SSD read":         "100 μs",
    "HDD read":         "10 ms",
    "Network (same DC)":"0.5 ms",
    "Network (cross DC)":"150 ms",
    "Redis GET":        "< 1 ms",
    "DB query (indexed)":"1-10 ms",
    "DB query (no index)":"100ms - seconds",
}
for k, v in numbers.items():
    print(f"  {k:25}: {v}")

# GraphQL - Query language for APIs
# pip install strawberry-graphql fastapi uvicorn

print("=== What is GraphQL? ===")
concepts = {
    "GraphQL":      "Query language — client asks exactly what data it needs",
    "Schema":       "Defines all types, queries, mutations available",
    "Query":        "Read data (like GET in REST)",
    "Mutation":     "Write/update/delete data (like POST/PUT/DELETE)",
    "Subscription": "Real-time data via WebSocket",
    "Resolver":     "Function that fetches data for a field",
    "Type":         "Shape of data (like a class/model)",
    "Field":        "One property of a type",
    "Argument":     "Parameter passed to a query/mutation",
}
for k, v in concepts.items():
    print(f"  {k:14}: {v}")

print("\n=== REST vs GraphQL ===")
print("""
  REST:
    GET /users/1              → returns ALL user fields
    GET /users/1/orders       → separate request for orders
    GET /users/1/address      → another request for address
    = 3 requests, over-fetching data you don't need

  GraphQL (single request):
    query {
      user(id: 1) {
        name              ← only what you need
        orders {
          product
          amount
        }
      }
    }
    = 1 request, exactly the data you asked for
""")

print("=== GraphQL Advantages ===")
pros = [
    "No over-fetching — get only fields you need",
    "No under-fetching — get nested data in one request",
    "Strongly typed schema — auto-documentation",
    "Single endpoint (/graphql) instead of many REST endpoints",
    "Great for mobile apps (save bandwidth)",
    "Introspection — clients can discover available queries",
]
for p in pros:
    print(f"  + {p}")

print("\n=== When to Use GraphQL ===")
print("  Use GraphQL: complex data requirements, mobile apps, multiple clients")
print("  Use REST:    simple CRUD, public APIs, file uploads, caching needs")

print("\n=== Install ===")
print("  pip install strawberry-graphql[fastapi] uvicorn")

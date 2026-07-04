# Microservices - Split app into small independent services

print("=== Monolith vs Microservices ===")
print("""
  MONOLITH                          MICROSERVICES
  ─────────────────────────────     ─────────────────────────────
  One big app                       Many small apps
  All code in one repo              Each service has own repo
  One database                      Each service has own DB
  Deploy everything together        Deploy each service independently
  Easy to start                     Complex to manage
  Hard to scale specific parts      Scale only what needs scaling
  One failure can crash all         One failure is isolated
""")

print("=== When to Use Microservices ===")
print("  Use Monolith when: small team, early stage, simple app")
print("  Use Microservices when: large team, high scale, different tech needs\n")

print("=== Example: E-commerce App Split ===")
services = {
    "User Service":     "Register, login, profile — port 8001",
    "Product Service":  "Catalog, search, inventory — port 8002",
    "Order Service":    "Cart, checkout, order history — port 8003",
    "Payment Service":  "Process payments, refunds — port 8004",
    "Email Service":    "Send emails, notifications — port 8005",
    "API Gateway":      "Single entry point, routes to services — port 8000",
}
for service, desc in services.items():
    print(f"  {service:18}: {desc}")

print("\n=== Communication Between Services ===")
comm = {
    "REST HTTP":    "Simple, synchronous — service calls another service's API",
    "Message Queue":"Async — Kafka/RabbitMQ — fire and forget",
    "gRPC":         "Fast binary protocol — good for internal service calls",
    "GraphQL":      "Flexible queries — good for API gateway",
}
for k, v in comm.items():
    print(f"  {k:16}: {v}")

print("\n=== Key Challenges ===")
challenges = [
    "Service discovery — how services find each other",
    "Distributed tracing — track request across services",
    "Data consistency — each service has own DB",
    "Network failures — handle timeouts and retries",
    "Authentication — JWT passed between services",
]
for c in challenges:
    print(f"  - {c}")

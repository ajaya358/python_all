# Message Queues - Async communication between services

print("=== What is a Message Queue? ===")
print("  Decouple services — producer sends message, consumer processes later")
print("  Producer doesn't wait for consumer to finish\n")

print("=== Why Use Message Queues? ===")
reasons = [
    "Decouple services — producer and consumer independent",
    "Handle traffic spikes — queue absorbs burst, workers process steadily",
    "Retry on failure — message stays in queue until processed",
    "Async processing — user gets instant response, work done in background",
    "Load leveling — smooth out uneven traffic",
]
for r in reasons:
    print(f"  - {r}")

print("\n=== Message Queue Tools ===")
tools = {
    "Redis (List/Stream)": "Simple, fast, good for small scale",
    "Celery + Redis":      "Best for Python background tasks",
    "RabbitMQ":            "Traditional queue, complex routing, reliable",
    "Apache Kafka":        "High throughput, persistent, replay, streaming",
    "AWS SQS":             "Managed queue, serverless, integrates with Lambda",
    "AWS SNS":             "Pub/Sub notifications, fan-out to multiple queues",
}
for k, v in tools.items():
    print(f"  {k:22}: {v}")

print("\n=== Queue Patterns ===")
print("""
  1. Point-to-Point (Queue)
     Producer → [Queue] → Consumer
     One message consumed by ONE consumer
     Use: task processing, job queue
  
  2. Pub/Sub (Topic)
     Publisher → [Topic] → Consumer 1
                         → Consumer 2
                         → Consumer 3
     One message consumed by ALL subscribers
     Use: notifications, event broadcasting
  
  3. Fan-out
     SNS Topic → SQS Queue 1 → Email Service
               → SQS Queue 2 → SMS Service
               → SQS Queue 3 → Push Notification
""")

print("=== Real Example: Order Processing ===")
print("""
  User places order:
  
  API → publishes "order.created" event
  
  Consumers:
  ├── Inventory Service  → reduce stock
  ├── Email Service      → send confirmation email
  ├── Payment Service    → process payment
  ├── Analytics Service  → record sale
  └── Notification Svc   → push notification
  
  All happen in parallel, independently, without blocking the API
""")

print("=== Dead Letter Queue (DLQ) ===")
print("  If message fails after N retries → moved to DLQ")
print("  Team can inspect DLQ to find and fix failed messages")
print("  Prevents poison messages from blocking the queue")

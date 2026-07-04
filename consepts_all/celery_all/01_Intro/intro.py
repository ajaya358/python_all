# Celery - Background Task Queue
# Run heavy tasks in background without blocking the API response
# pip install celery redis

print("=== What is Celery? ===")
concepts = {
    "Celery":   "Task queue — runs functions in background workers",
    "Broker":   "Message queue that holds tasks (Redis or RabbitMQ)",
    "Worker":   "Process that picks up and runs tasks",
    "Task":     "A Python function decorated with @celery.task",
    "Result":   "Task output stored in backend (Redis/DB)",
    "Beat":     "Celery scheduler — runs tasks on a schedule (like cron)",
}
for k, v in concepts.items():
    print(f"  {k:10}: {v}")

print("\n=== Why Use Celery? ===")
use_cases = [
    "Send email after user registers (don't make user wait)",
    "Generate PDF report in background",
    "Process uploaded image/video",
    "Send bulk notifications",
    "Scrape data periodically",
    "Run ML model inference on large data",
    "Sync data with third-party APIs",
]
for u in use_cases:
    print(f"  - {u}")

print("\n=== How It Works ===")
flow = [
    "1. FastAPI receives request",
    "2. FastAPI sends task to Redis broker (instantly returns response)",
    "3. Celery worker picks up task from Redis",
    "4. Worker runs the task in background",
    "5. Result stored in Redis backend",
    "6. Client can poll for result if needed",
]
for step in flow:
    print(f"  {step}")

print("\n=== Install & Run ===")
print("  pip install celery redis")
print("  Start Redis: docker run -d -p 6379:6379 redis")
print("  Start worker: celery -A tasks worker --loglevel=info")
print("  Start beat:   celery -A tasks beat --loglevel=info")

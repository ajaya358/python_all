# Celery Basic Tasks
# pip install celery redis
# Start Redis: docker run -d -p 6379:6379 redis
# Run worker: celery -A basic_tasks worker --loglevel=info

from celery import Celery
import time

# --- Setup Celery with Redis as broker and backend ---
app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

# --- Define Tasks ---
@app.task
def add(x, y):
    return x + y

@app.task
def send_email(to_email: str, subject: str):
    time.sleep(2)  # simulate email sending delay
    print(f"Email sent to {to_email}: {subject}")
    return f"Email delivered to {to_email}"

@app.task
def process_data(items: list):
    time.sleep(3)  # simulate heavy processing
    result = [item.upper() for item in items]
    return result

@app.task(bind=True, max_retries=3)
def fetch_from_api(self, url: str):
    try:
        # simulate API call
        if "fail" in url:
            raise Exception("API failed")
        return f"Data from {url}"
    except Exception as exc:
        raise self.retry(exc=exc, countdown=5)  # retry after 5 seconds

# --- How to call tasks ---
print("=== Calling Tasks ===")
print()
print("# Async (background) — returns immediately")
print("result = add.delay(4, 6)")
print("print(result.id)          # task ID")
print("print(result.status)      # PENDING / SUCCESS / FAILURE")
print("print(result.get())       # wait and get result → 10")
print()
print("# Apply async with options")
print("send_email.apply_async(args=['user@email.com', 'Welcome!'], countdown=10)")
print("# countdown=10 → run after 10 seconds")
print()
print("# Chain tasks (output of one goes to next)")
print("from celery import chain")
print("chain(add.s(2, 3), add.s(10)).delay()  # (2+3)+10 = 15")

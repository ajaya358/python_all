# Celery + FastAPI Integration
# API returns immediately, heavy work runs in background
# pip install fastapi uvicorn celery redis
# Start Redis: docker run -d -p 6379:6379 redis
# Start worker: celery -A celery_fastapi worker --loglevel=info
# Run API: uvicorn celery_fastapi:app --reload

from fastapi import FastAPI
from celery import Celery
import time

# --- Celery setup ---
celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

# --- Celery Tasks ---
@celery_app.task
def send_welcome_email(email: str, name: str):
    time.sleep(3)  # simulate email delay
    print(f"Welcome email sent to {email}")
    return {"status": "sent", "to": email}

@celery_app.task
def generate_report(user_id: int):
    time.sleep(5)  # simulate report generation
    return {"report": f"Report for user {user_id}", "pages": 10}

@celery_app.task
def process_image(filename: str):
    time.sleep(4)  # simulate image processing
    return {"processed": filename, "size": "1024x768"}

# --- FastAPI App ---
app = FastAPI()

@app.post("/register")
def register_user(name: str, email: str):
    # Send email in background — API returns instantly
    task = send_welcome_email.delay(email, name)
    return {
        "message": f"User {name} registered successfully",
        "email_task_id": task.id
    }

@app.post("/report/{user_id}")
def request_report(user_id: int):
    task = generate_report.delay(user_id)
    return {"message": "Report generation started", "task_id": task.id}

@app.get("/task/{task_id}")
def get_task_status(task_id: str):
    task = celery_app.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": task.status,       # PENDING, STARTED, SUCCESS, FAILURE
        "result": task.result if task.ready() else None
    }

# Run: uvicorn celery_fastapi:app --reload
# POST /register?name=Ajay&email=ajay@email.com
# GET  /task/<task_id>  → check status

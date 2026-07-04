# Celery Scheduled Tasks (Celery Beat)
# Run tasks automatically on a schedule — like cron jobs
# Run beat: celery -A scheduled_tasks beat --loglevel=info
# Run worker: celery -A scheduled_tasks worker --loglevel=info

from celery import Celery
from celery.schedules import crontab

app = Celery(
    "scheduled",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

# --- Scheduled Tasks Config ---
app.conf.beat_schedule = {
    # Run every 30 seconds
    "check-health-every-30s": {
        "task": "scheduled_tasks.health_check",
        "schedule": 30.0,
    },
    # Run every minute
    "sync-data-every-minute": {
        "task": "scheduled_tasks.sync_data",
        "schedule": 60.0,
    },
    # Run every day at 8:00 AM
    "daily-report-8am": {
        "task": "scheduled_tasks.send_daily_report",
        "schedule": crontab(hour=8, minute=0),
    },
    # Run every Monday at 9:00 AM
    "weekly-cleanup-monday": {
        "task": "scheduled_tasks.cleanup_old_data",
        "schedule": crontab(hour=9, minute=0, day_of_week=1),
    },
    # Run on 1st of every month
    "monthly-billing": {
        "task": "scheduled_tasks.process_billing",
        "schedule": crontab(day_of_month=1, hour=0, minute=0),
    },
}

# --- Task Definitions ---
@app.task
def health_check():
    print("Health check: system OK")
    return "OK"

@app.task
def sync_data():
    print("Syncing data with external API...")
    return "Synced"

@app.task
def send_daily_report():
    print("Sending daily report email to admin...")
    return "Report sent"

@app.task
def cleanup_old_data():
    print("Cleaning up records older than 90 days...")
    return "Cleanup done"

@app.task
def process_billing():
    print("Processing monthly billing for all users...")
    return "Billing done"

print("=== Crontab Reference ===")
cron_examples = {
    "crontab()":                          "Every minute",
    "crontab(minute=0)":                  "Every hour",
    "crontab(hour=8, minute=0)":          "Every day at 8 AM",
    "crontab(day_of_week=1)":             "Every Monday",
    "crontab(day_of_month=1)":            "1st of every month",
    "crontab(month_of_year=1, day=1)":    "Every Jan 1st",
}
for expr, desc in cron_examples.items():
    print(f"  {expr:45}: {desc}")

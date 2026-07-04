# Kafka + FastAPI - Event-driven API
# pip install fastapi uvicorn kafka-python
# Start Kafka: docker-compose up -d

from fastapi import FastAPI
from kafka import KafkaProducer, KafkaConsumer
import json
import threading

app = FastAPI()

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)

def publish_event(topic: str, event: dict):
    producer.send(topic, value=event)
    producer.flush()

@app.post("/users/register")
def register_user(name: str, email: str):
    publish_event("user-registered", {"user_id": 1, "email": email, "name": name})
    return {"message": f"User {name} registered", "email_task": "queued"}

@app.post("/orders")
def create_order(user_id: int, product: str, amount: float):
    order = {"order_id": 101, "user_id": user_id, "product": product, "amount": amount}
    publish_event("order-created", order)
    return {"message": "Order created", "order": order}

@app.post("/payments")
def process_payment(order_id: int, amount: float):
    publish_event("payment-processed", {"order_id": order_id, "amount": amount, "status": "success"})
    return {"message": "Payment processed"}

def start_consumer():
    consumer = KafkaConsumer(
        'user-registered',
        bootstrap_servers=['localhost:9092'],
        group_id='email-service',
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='latest',
    )
    for message in consumer:
        event = message.value
        print(f"[Email Service] Sending welcome email to {event['email']}")

@app.on_event("startup")
def startup():
    thread = threading.Thread(target=start_consumer, daemon=True)
    thread.start()

@app.on_event("shutdown")
def shutdown():
    producer.close()

# Run: uvicorn kafka_fastapi:app --reload
# Flow: POST /users/register → publishes event → consumer sends email

# Redis Pub/Sub - Publish and Subscribe messaging
# pip install redis

import redis
import threading
import time
import json

# --- Publisher ---
def publisher():
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    time.sleep(1)  # wait for subscriber to connect

    events = [
        {"type": "user_registered", "user_id": 1, "email": "ajay@email.com"},
        {"type": "order_created",   "order_id": 101, "amount": 5000},
        {"type": "payment_done",    "order_id": 101, "status": "success"},
    ]

    for event in events:
        channel = f"events:{event['type']}"
        r.publish(channel, json.dumps(event))
        print(f"  [PUB] Published to {channel}: {event}")
        time.sleep(0.5)

# --- Subscriber ---
def subscriber():
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    pubsub = r.pubsub()

    # Subscribe to specific channels
    pubsub.subscribe('events:user_registered', 'events:order_created', 'events:payment_done')
    print("  [SUB] Subscribed to channels, waiting for messages...")

    for message in pubsub.listen():
        if message['type'] == 'message':
            data = json.loads(message['data'])
            print(f"  [SUB] Received on {message['channel']}: {data}")

# --- Pattern Subscribe (wildcard) ---
def pattern_subscriber():
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    pubsub = r.pubsub()
    pubsub.psubscribe('events:*')  # subscribe to all events:* channels

    for message in pubsub.listen():
        if message['type'] == 'pmessage':
            print(f"  [PATTERN SUB] {message['channel']}: {message['data']}")

print("=== Redis Pub/Sub Demo ===")
print("  Starting subscriber and publisher threads...\n")

sub_thread = threading.Thread(target=subscriber, daemon=True)
pub_thread = threading.Thread(target=publisher, daemon=True)

sub_thread.start()
pub_thread.start()
pub_thread.join()
time.sleep(1)

print("\n=== Pub/Sub vs Kafka ===")
comparison = {
    "Redis Pub/Sub": "No persistence, message lost if no subscriber, simple, fast",
    "Kafka":         "Persistent, replay messages, consumer groups, high throughput",
}
for k, v in comparison.items():
    print(f"  {k:16}: {v}")

print("\n=== Use Cases ===")
uses = [
    "Real-time notifications (new message, order update)",
    "Live dashboard updates",
    "Chat applications",
    "Invalidate cache across multiple servers",
    "Broadcast events to multiple services",
]
for u in uses:
    print(f"  - {u}")

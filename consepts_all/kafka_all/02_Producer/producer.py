# Kafka Producer - Send messages to Kafka topics
# pip install kafka-python
# Start Kafka: docker-compose up -d (see intro.py)

from kafka import KafkaProducer
import json
import time

# --- Basic Producer ---
print("=== Kafka Producer ===")
print("""
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: k.encode('utf-8') if k else None,
)

# Send a message
producer.send(
    topic='user-events',
    key='user_1',
    value={'event': 'login', 'user_id': 1, 'timestamp': '2024-01-01T10:00:00'}
)

# Flush — wait for all messages to be sent
producer.flush()
producer.close()
print("Message sent!")
""")

print("=== Producer with Callbacks ===")
print("""
def on_success(metadata):
    print(f"Sent to topic={metadata.topic}, partition={metadata.partition}, offset={metadata.offset}")

def on_error(exception):
    print(f"Failed to send: {exception}")

producer.send('user-events', value={'event': 'purchase'}).add_callback(on_success).add_errback(on_error)
producer.flush()
""")

print("=== Batch Producer (high throughput) ===")
print("""
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    batch_size=16384,       # batch up to 16KB before sending
    linger_ms=10,           # wait 10ms to collect more messages
    compression_type='gzip' # compress messages
)

# Send 1000 events
for i in range(1000):
    producer.send('orders', value={'order_id': i, 'amount': i * 100})

producer.flush()
print("1000 messages sent!")
""")

print("=== Common Producer Config ===")
config = {
    "bootstrap_servers":  "Kafka broker addresses",
    "value_serializer":   "How to convert Python object to bytes",
    "key_serializer":     "How to convert key to bytes",
    "acks":               "0=no ack, 1=leader ack, all=all replicas ack",
    "retries":            "Retry on failure (default 0)",
    "batch_size":         "Max bytes per batch",
    "linger_ms":          "Wait time to fill batch",
    "compression_type":   "gzip/snappy/lz4 to reduce size",
}
for k, v in config.items():
    print(f"  {k:20}: {v}")

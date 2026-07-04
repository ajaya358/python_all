# Kafka Consumer - Read messages from Kafka topics
# pip install kafka-python

print("=== Basic Consumer ===")
print("""
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'user-events',                              # topic name
    bootstrap_servers=['localhost:9092'],
    group_id='user-events-group',               # consumer group
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',               # start from beginning if no offset
    enable_auto_commit=True,                    # auto commit offset
)

print("Listening for messages...")
for message in consumer:
    print(f"Topic: {message.topic}")
    print(f"Partition: {message.partition}")
    print(f"Offset: {message.offset}")
    print(f"Key: {message.key}")
    print(f"Value: {message.value}")
    print("---")
""")

print("=== Consumer Group (parallel processing) ===")
print("""
# Run 3 consumers in same group → each gets different partitions
# consumer1.py, consumer2.py, consumer3.py all use group_id='order-processors'

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers=['localhost:9092'],
    group_id='order-processors',   # same group = load balanced
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
)

for message in consumer:
    order = message.value
    print(f"Processing order: {order['order_id']}")
    # process order...
""")

print("=== Manual Commit (for reliability) ===")
print("""
consumer = KafkaConsumer(
    'payments',
    bootstrap_servers=['localhost:9092'],
    group_id='payment-processors',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    enable_auto_commit=False,   # manual commit
)

for message in consumer:
    try:
        process_payment(message.value)
        consumer.commit()       # only commit after successful processing
    except Exception as e:
        print(f"Failed: {e}")
        # don't commit — message will be reprocessed
""")

print("=== Subscribe to Multiple Topics ===")
print("""
consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    group_id='my-group',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
)
consumer.subscribe(['user-events', 'orders', 'payments'])

for message in consumer:
    if message.topic == 'user-events':
        handle_user_event(message.value)
    elif message.topic == 'orders':
        handle_order(message.value)
""")

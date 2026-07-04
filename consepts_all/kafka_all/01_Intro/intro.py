# Apache Kafka - Distributed Message Streaming Platform
# pip install kafka-python

print("=== What is Kafka? ===")
concepts = {
    "Kafka":        "Distributed event streaming platform — high throughput message queue",
    "Producer":     "App that sends (publishes) messages to Kafka",
    "Consumer":     "App that reads (subscribes to) messages from Kafka",
    "Topic":        "Category/channel for messages (like a queue name)",
    "Partition":    "Topic split into parts for parallel processing",
    "Broker":       "Kafka server that stores messages",
    "Cluster":      "Group of Kafka brokers",
    "Offset":       "Position of a message in a partition",
    "Consumer Group":"Multiple consumers sharing work on same topic",
    "Retention":    "How long Kafka keeps messages (default 7 days)",
}
for k, v in concepts.items():
    print(f"  {k:16}: {v}")

print("\n=== Kafka vs Redis Pub/Sub ===")
comparison = {
    "Kafka":        "Persistent, replay messages, high throughput, ordered, partitioned",
    "Redis Pub/Sub":"In-memory, no persistence, simpler, lower latency for small scale",
    "RabbitMQ":     "Traditional queue, complex routing, good for task queues",
    "Celery+Redis": "Best for background tasks in Python apps",
}
for k, v in comparison.items():
    print(f"  {k:14}: {v}")

print("\n=== When to Use Kafka ===")
use_cases = [
    "Real-time analytics (user clicks, page views)",
    "Event sourcing (log every state change)",
    "Microservices communication (async events)",
    "Data pipeline (ETL — extract, transform, load)",
    "Log aggregation from multiple services",
    "Stream processing (fraud detection, recommendations)",
]
for u in use_cases:
    print(f"  - {u}")

print("\n=== Start Kafka with Docker ===")
print("""
# docker-compose.yml
version: '3.8'
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:7.4.0
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181

  kafka:
    image: confluentinc/cp-kafka:7.4.0
    depends_on: [zookeeper]
    ports:
      - "9092:9092"
    environment:
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_AUTO_CREATE_TOPICS_ENABLE: 'true'

# Start: docker-compose up -d
""")

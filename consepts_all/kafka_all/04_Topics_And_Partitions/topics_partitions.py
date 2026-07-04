# Kafka Topics and Partitions - Core architecture concepts

print("=== Topics ===")
print("  Topic = named channel for messages (like a table in DB)")
print("  Producers write to topics, consumers read from topics\n")

print("=== Partitions ===")
print("""
  Topic 'orders' with 3 partitions:

  Partition 0: [msg0] [msg3] [msg6] [msg9]  ← Consumer 1
  Partition 1: [msg1] [msg4] [msg7]          ← Consumer 2
  Partition 2: [msg2] [msg5] [msg8]          ← Consumer 3

  - Messages with same key always go to same partition (ordering guaranteed)
  - More partitions = more parallelism = higher throughput
  - Each partition is ordered, but no ordering across partitions
""")

print("=== Kafka CLI Commands ===")
print("""
# Create topic
kafka-topics.sh --create \\
  --bootstrap-server localhost:9092 \\
  --topic user-events \\
  --partitions 3 \\
  --replication-factor 1

# List topics
kafka-topics.sh --list --bootstrap-server localhost:9092

# Describe topic
kafka-topics.sh --describe --topic user-events --bootstrap-server localhost:9092

# Delete topic
kafka-topics.sh --delete --topic user-events --bootstrap-server localhost:9092

# Produce messages (terminal)
kafka-console-producer.sh --topic user-events --bootstrap-server localhost:9092

# Consume messages (terminal)
kafka-console-consumer.sh --topic user-events --from-beginning --bootstrap-server localhost:9092
""")

print("=== Create Topic with Python ===")
print("""
from kafka.admin import KafkaAdminClient, NewTopic

admin = KafkaAdminClient(bootstrap_servers=['localhost:9092'])

topics = [
    NewTopic(name='user-events',  num_partitions=3, replication_factor=1),
    NewTopic(name='orders',       num_partitions=5, replication_factor=1),
    NewTopic(name='notifications',num_partitions=2, replication_factor=1),
]
admin.create_topics(new_topics=topics)
print("Topics created!")
""")

print("=== Partition Key Strategy ===")
strategies = {
    "user_id as key":    "All events for same user go to same partition (ordered per user)",
    "order_id as key":   "All events for same order stay together",
    "None (no key)":     "Round-robin across partitions (max throughput)",
    "region as key":     "Events grouped by region",
}
for k, v in strategies.items():
    print(f"  {k:22}: {v}")

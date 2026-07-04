# Databases in System Design - Choose the right DB

print("=== SQL vs NoSQL ===")
print("""
  SQL (Relational):                   NoSQL:
  ─────────────────────────────────   ─────────────────────────────────
  Structured data (tables/rows)       Flexible schema (JSON documents)
  Strong consistency (ACID)           Eventual consistency (BASE)
  Complex queries with JOINs          Simple queries, no JOINs
  Vertical scaling mainly             Horizontal scaling built-in
  PostgreSQL, MySQL                   MongoDB, DynamoDB, Cassandra
  
  Use SQL when:                       Use NoSQL when:
  - Data has clear relationships      - Unstructured/flexible data
  - Need complex queries              - Need massive horizontal scale
  - Financial/transactional data      - High write throughput
  - Strong consistency needed         - Simple access patterns
""")

print("=== Database Types ===")
db_types = {
    "Relational (SQL)":     "PostgreSQL, MySQL — structured data, ACID, JOINs",
    "Document":             "MongoDB — JSON documents, flexible schema",
    "Key-Value":            "Redis, DynamoDB — fast lookups by key",
    "Wide-Column":          "Cassandra, HBase — huge scale, time-series",
    "Graph":                "Neo4j — relationships (social networks, fraud)",
    "Search":               "Elasticsearch — full-text search, analytics",
    "Time-Series":          "InfluxDB, TimescaleDB — metrics, IoT data",
    "Vector":               "ChromaDB, Pinecone — AI embeddings, semantic search",
}
for k, v in db_types.items():
    print(f"  {k:22}: {v}")

print("\n=== Database Scaling Patterns ===")
print("""
  1. Read Replicas
     Master (writes) → Replica 1 (reads)
                     → Replica 2 (reads)
                     → Replica 3 (reads)
     
  2. Sharding (Horizontal Partitioning)
     Shard by user_id:
     user_id 1-1M    → DB Shard 1
     user_id 1M-2M   → DB Shard 2
     user_id 2M-3M   → DB Shard 3
     
  3. CQRS (Command Query Responsibility Segregation)
     Write operations → Write DB (normalized)
     Read operations  → Read DB (denormalized, optimized for reads)
""")

print("=== ACID vs BASE ===")
print("  ACID (SQL):  Atomicity, Consistency, Isolation, Durability")
print("               → All or nothing, always consistent, safe")
print()
print("  BASE (NoSQL): Basically Available, Soft state, Eventually consistent")
print("                → Always available, data syncs eventually")

print("\n=== Which DB for What? ===")
use_cases = {
    "User profiles, orders":        "PostgreSQL",
    "Product catalog":              "PostgreSQL or MongoDB",
    "Sessions, caching":            "Redis",
    "Chat messages":                "Cassandra (high write)",
    "Search functionality":         "Elasticsearch",
    "Social graph (followers)":     "Neo4j",
    "Analytics, logs":              "ClickHouse or Elasticsearch",
    "AI/RAG embeddings":            "ChromaDB or Pinecone",
    "IoT sensor data":              "InfluxDB",
}
for use, db in use_cases.items():
    print(f"  {use:35}: {db}")

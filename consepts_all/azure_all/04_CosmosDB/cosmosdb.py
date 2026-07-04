# Azure Cosmos DB - Globally distributed NoSQL database
# Like AWS DynamoDB but with multiple API options
# pip install azure-cosmos

print("=== Cosmos DB Concepts ===")
concepts = {
    "Account":      "Top-level resource — choose API and consistency level",
    "Database":     "Container for collections",
    "Container":    "Like a table — stores items",
    "Item":         "JSON document (like MongoDB document)",
    "Partition Key":"Field used to distribute data across partitions",
    "RU/s":         "Request Units per second — billing and throughput unit",
    "TTL":          "Auto-delete items after N seconds",
    "Change Feed":  "Stream of all changes — trigger functions on data change",
}
for k, v in concepts.items():
    print(f"  {k:16}: {v}")

print("\n=== Cosmos DB APIs ===")
apis = {
    "NoSQL (Core)": "Native JSON documents — recommended for new projects",
    "MongoDB":      "Use MongoDB drivers — easy migration from MongoDB",
    "Cassandra":    "Use Cassandra drivers — wide-column store",
    "Gremlin":      "Graph database API",
    "Table":        "Key-value like Azure Table Storage",
}
for k, v in apis.items():
    print(f"  {k:16}: {v}")

print("\n=== CRUD Operations ===")
print("""
from azure.cosmos import CosmosClient, PartitionKey

# Connect
client = CosmosClient(url="https://myaccount.documents.azure.com:443/", credential="mykey")

# Get database and container
db = client.get_database_client("mydb")
container = db.get_container_client("users")

# CREATE container (one-time)
db.create_container_if_not_exists(
    id="users",
    partition_key=PartitionKey(path="/city")
)

# CREATE item
user = {
    "id": "user_001",
    "name": "Ajay",
    "email": "ajay@email.com",
    "city": "Chennai",      # partition key
    "age": 25
}
container.create_item(body=user)

# READ item
item = container.read_item(item="user_001", partition_key="Chennai")
print(item)

# UPDATE item (upsert = create or replace)
user["age"] = 26
container.upsert_item(body=user)

# DELETE item
container.delete_item(item="user_001", partition_key="Chennai")

# QUERY items
query = "SELECT * FROM c WHERE c.city = 'Chennai' AND c.age > 20"
items = list(container.query_items(query=query, enable_cross_partition_query=True))
for item in items:
    print(item["name"])

# Query with parameters (safe from injection)
query = "SELECT * FROM c WHERE c.city = @city"
params = [{"name": "@city", "value": "Chennai"}]
items = list(container.query_items(query=query, parameters=params))
""")

print("=== Consistency Levels ===")
levels = {
    "Strong":           "Always reads latest data — slowest",
    "Bounded Staleness":"Reads data within N seconds/operations old",
    "Session":          "Consistent within same session — default, recommended",
    "Consistent Prefix":"Reads in order, may be slightly stale",
    "Eventual":         "Fastest, least consistent — reads may be stale",
}
for k, v in levels.items():
    print(f"  {k:22}: {v}")

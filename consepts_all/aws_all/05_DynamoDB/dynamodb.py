# AWS DynamoDB - Managed NoSQL Database
# Key-value + document store, serverless, auto-scales
# pip install boto3

print("=== DynamoDB Key Concepts ===")
concepts = {
    "Table":            "Container for items (like a collection in MongoDB)",
    "Item":             "One record (like a row in SQL or document in MongoDB)",
    "Attribute":        "Field of an item (like a column)",
    "Partition Key":    "Primary key — determines which partition stores item",
    "Sort Key":         "Optional secondary key — enables range queries",
    "GSI":              "Global Secondary Index — query by non-primary key",
    "LSI":              "Local Secondary Index — alternate sort key",
    "Capacity Units":   "RCU (read) and WCU (write) — billing units",
    "On-Demand":        "Auto-scale, pay per request — good for variable traffic",
}
for k, v in concepts.items():
    print(f"  {k:18}: {v}")

print("\n=== CRUD Operations ===")
print("""
import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('Users')

# CREATE TABLE (one-time setup)
dynamodb.create_table(
    TableName='Users',
    KeySchema=[
        {'AttributeName': 'user_id', 'KeyType': 'HASH'},   # Partition key
        {'AttributeName': 'email',   'KeyType': 'RANGE'},  # Sort key
    ],
    AttributeDefinitions=[
        {'AttributeName': 'user_id', 'AttributeType': 'S'},
        {'AttributeName': 'email',   'AttributeType': 'S'},
    ],
    BillingMode='PAY_PER_REQUEST'
)

# PUT ITEM (create/replace)
table.put_item(Item={
    'user_id': 'user_001',
    'email': 'ajay@email.com',
    'name': 'Ajay',
    'age': 25,
    'tags': ['python', 'fastapi']
})

# GET ITEM
response = table.get_item(Key={'user_id': 'user_001', 'email': 'ajay@email.com'})
item = response.get('Item')
print(item)

# UPDATE ITEM
table.update_item(
    Key={'user_id': 'user_001', 'email': 'ajay@email.com'},
    UpdateExpression='SET age = :age, #n = :name',
    ExpressionAttributeValues={':age': 26, ':name': 'Ajay Kumar'},
    ExpressionAttributeNames={'#n': 'name'}
)

# DELETE ITEM
table.delete_item(Key={'user_id': 'user_001', 'email': 'ajay@email.com'})

# QUERY (by partition key)
response = table.query(
    KeyConditionExpression='user_id = :uid',
    ExpressionAttributeValues={':uid': 'user_001'}
)
items = response['Items']

# SCAN (full table scan — avoid for large tables)
response = table.scan(
    FilterExpression='age > :age',
    ExpressionAttributeValues={':age': 20}
)
""")

print("=== When to Use DynamoDB ===")
use_cases = [
    "Session storage (user sessions with TTL)",
    "User profiles with flexible attributes",
    "IoT device data (high write throughput)",
    "Gaming leaderboards (sorted sets)",
    "Shopping cart (per-user items)",
    "Event logs (partition by date)",
]
for u in use_cases:
    print(f"  - {u}")

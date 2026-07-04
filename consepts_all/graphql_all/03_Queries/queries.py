# GraphQL Queries - Read data
# pip install strawberry-graphql[fastapi] uvicorn
# Run: uvicorn queries:app --reload
# Open: http://localhost:8000/graphql  (GraphiQL playground)

import strawberry
from typing import List, Optional
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# --- Fake data ---
users_db = [
    {"id": 1, "name": "Ajay",  "email": "ajay@email.com",  "age": 25},
    {"id": 2, "name": "Ravi",  "email": "ravi@email.com",  "age": 30},
    {"id": 3, "name": "Priya", "email": "priya@email.com", "age": 22},
]
products_db = [
    {"id": 1, "name": "Laptop", "price": 50000.0, "category": "Electronics"},
    {"id": 2, "name": "Phone",  "price": 20000.0, "category": "Electronics"},
    {"id": 3, "name": "Book",   "price": 500.0,   "category": "Education"},
]

# --- Types ---
@strawberry.type
class User:
    id: int
    name: str
    email: str
    age: Optional[int] = None

@strawberry.type
class Product:
    id: int
    name: str
    price: float
    category: str

# --- Query Resolvers ---
@strawberry.type
class Query:

    @strawberry.field
    def users(self) -> List[User]:
        return [User(**u) for u in users_db]

    @strawberry.field
    def user(self, id: int) -> Optional[User]:
        user = next((u for u in users_db if u["id"] == id), None)
        return User(**user) if user else None

    @strawberry.field
    def products(self, category: Optional[str] = None) -> List[Product]:
        if category:
            filtered = [p for p in products_db if p["category"] == category]
            return [Product(**p) for p in filtered]
        return [Product(**p) for p in products_db]

    @strawberry.field
    def search_users(self, name: str) -> List[User]:
        matched = [u for u in users_db if name.lower() in u["name"].lower()]
        return [User(**u) for u in matched]

# --- Schema and App ---
schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

# --- Example Queries (run in GraphiQL at /graphql) ---
print("=== Example GraphQL Queries ===")
print("""
# Get all users
query {
  users {
    id
    name
    email
  }
}

# Get specific user
query {
  user(id: 1) {
    name
    email
    age
  }
}

# Get products by category
query {
  products(category: "Electronics") {
    name
    price
  }
}

# Search users
query {
  searchUsers(name: "aj") {
    id
    name
  }
}
""")

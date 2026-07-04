# GraphQL Schema and Types with Strawberry
# pip install strawberry-graphql[fastapi]

import strawberry
from typing import List, Optional

# --- Define Types (like Pydantic models for GraphQL) ---
@strawberry.type
class Address:
    street: str
    city: str
    pincode: str

@strawberry.type
class Order:
    id: int
    product: str
    amount: float
    status: str

@strawberry.type
class User:
    id: int
    name: str
    email: str
    age: Optional[int] = None
    address: Optional[Address] = None
    orders: Optional[List[Order]] = None

@strawberry.type
class Product:
    id: int
    name: str
    price: float
    category: str
    in_stock: bool

# --- Input Types (for mutations) ---
@strawberry.input
class CreateUserInput:
    name: str
    email: str
    age: Optional[int] = None

@strawberry.input
class UpdateUserInput:
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None

# --- Enum Type ---
@strawberry.enum
class OrderStatus:
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

print("=== GraphQL SDL (Schema Definition Language) ===")
print("""
# This is what the schema looks like in SDL format:

type User {
  id: Int!              # ! means required (non-null)
  name: String!
  email: String!
  age: Int              # no ! means optional (nullable)
  address: Address
  orders: [Order]       # list of orders
}

type Order {
  id: Int!
  product: String!
  amount: Float!
  status: String!
}

input CreateUserInput {
  name: String!
  email: String!
  age: Int
}

enum OrderStatus {
  PENDING
  PROCESSING
  SHIPPED
  DELIVERED
}
""")

print("=== Scalar Types ===")
scalars = {
    "Int":      "Integer number",
    "Float":    "Decimal number",
    "String":   "Text",
    "Boolean":  "True/False",
    "ID":       "Unique identifier (string or int)",
    "Date":     "Custom scalar (strawberry.scalar)",
}
for k, v in scalars.items():
    print(f"  {k:10}: {v}")

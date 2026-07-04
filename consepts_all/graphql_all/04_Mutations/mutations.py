# GraphQL Mutations - Create, Update, Delete data
# pip install strawberry-graphql[fastapi] uvicorn
# Run: uvicorn mutations:app --reload

import strawberry
from typing import List, Optional
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# --- Fake DB ---
users_db = [
    {"id": 1, "name": "Ajay", "email": "ajay@email.com", "age": 25},
]
next_id = 2

# --- Types ---
@strawberry.type
class User:
    id: int
    name: str
    email: str
    age: Optional[int] = None

@strawberry.type
class DeleteResult:
    success: bool
    message: str

# --- Input Types ---
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

# --- Query ---
@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[User]:
        return [User(**u) for u in users_db]

# --- Mutations ---
@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_user(self, input: CreateUserInput) -> User:
        global next_id
        user = {"id": next_id, "name": input.name, "email": input.email, "age": input.age}
        users_db.append(user)
        next_id += 1
        return User(**user)

    @strawberry.mutation
    def update_user(self, id: int, input: UpdateUserInput) -> Optional[User]:
        for user in users_db:
            if user["id"] == id:
                if input.name is not None:
                    user["name"] = input.name
                if input.email is not None:
                    user["email"] = input.email
                if input.age is not None:
                    user["age"] = input.age
                return User(**user)
        return None

    @strawberry.mutation
    def delete_user(self, id: int) -> DeleteResult:
        global users_db
        before = len(users_db)
        users_db = [u for u in users_db if u["id"] != id]
        if len(users_db) < before:
            return DeleteResult(success=True, message=f"User {id} deleted")
        return DeleteResult(success=False, message=f"User {id} not found")

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

print("=== Example Mutations (run in GraphiQL at /graphql) ===")
print("""
# Create user
mutation {
  createUser(input: {name: "Priya", email: "priya@email.com", age: 22}) {
    id
    name
    email
  }
}

# Update user
mutation {
  updateUser(id: 1, input: {name: "Ajay Kumar", age: 26}) {
    id
    name
    age
  }
}

# Delete user
mutation {
  deleteUser(id: 2) {
    success
    message
  }
}
""")

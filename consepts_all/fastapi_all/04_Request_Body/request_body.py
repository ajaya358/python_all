from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

# POST - JSON body sent by client
@app.post("/register")
def register(user: User):
    return {"message": f"User {user.name} registered", "age": user.age}

# PUT - update existing data
@app.put("/update/{user_id}")
def update_user(user_id: int, user: User):
    return {"user_id": user_id, "updated_name": user.name}

# Run: uvicorn request_body:app --reload

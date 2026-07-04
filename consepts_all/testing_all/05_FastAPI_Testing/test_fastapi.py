# FastAPI Testing - Test your API endpoints
# pip install pytest httpx fastapi
# Run: pytest test_fastapi.py -v

import pytest
from fastapi import FastAPI, HTTPException, Depends
from fastapi.testclient import TestClient
from pydantic import BaseModel

# --- App to test ---
app = FastAPI()

fake_db = {
    1: {"id": 1, "name": "Ajay", "email": "ajay@email.com"},
    2: {"id": 2, "name": "Ravi", "email": "ravi@email.com"},
}

class UserCreate(BaseModel):
    name: str
    email: str

@app.get("/")
def root():
    return {"message": "Hello"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = fake_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    new_id = max(fake_db.keys()) + 1
    new_user = {"id": new_id, **user.dict()}
    fake_db[new_id] = new_user
    return new_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    del fake_db[user_id]
    return {"message": "Deleted"}

# --- Test Client ---
client = TestClient(app)

# --- Tests ---
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}

def test_get_existing_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Ajay"
    assert data["email"] == "ajay@email.com"

def test_get_missing_user():
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_create_user():
    payload = {"name": "Priya", "email": "priya@email.com"}
    response = client.post("/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Priya"
    assert "id" in data

def test_delete_user():
    response = client.delete("/users/2")
    assert response.status_code == 200
    # Verify deleted
    response = client.get("/users/2")
    assert response.status_code == 404

def test_delete_missing_user():
    response = client.delete("/users/999")
    assert response.status_code == 404

# --- Test with Auth Header ---
def test_with_auth_header():
    response = client.get(
        "/users/1",
        headers={"Authorization": "Bearer fake-token"}
    )
    assert response.status_code == 200

# --- Fixture for client ---
@pytest.fixture
def test_client():
    return TestClient(app)

def test_using_fixture(test_client):
    response = test_client.get("/")
    assert response.status_code == 200

# Run: pytest test_fastapi.py -v

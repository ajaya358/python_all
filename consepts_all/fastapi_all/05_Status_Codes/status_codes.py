from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

# 200 OK (default)
@app.get("/ok")
def ok():
    return {"status": "OK"}

# 201 Created
@app.post("/create", status_code=201)
def create():
    return {"message": "Resource created"}

# 404 Not Found
@app.get("/item/{item_id}")
def get_item(item_id: int):
    if item_id != 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}

# 400 Bad Request
@app.get("/validate/{age}")
def validate_age(age: int):
    if age < 0:
        raise HTTPException(status_code=400, detail="Age cannot be negative")
    return {"age": age}

# Run: uvicorn status_codes:app --reload

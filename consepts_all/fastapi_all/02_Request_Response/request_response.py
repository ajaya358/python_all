from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

# GET - returns a response
@app.get("/item")
def get_item():
    return {"name": "Apple", "price": 1.5}

# POST - receives request body, returns response
@app.post("/item")
def create_item(item: Item):
    return {"received": item.name, "price": item.price}

# Run: uvicorn request_response:app --reload

from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class Product(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: float = Field(gt=0, description="Price must be greater than 0")
    quantity: int = Field(ge=1, description="At least 1 item")

class UserSignup(BaseModel):
    username: str = Field(min_length=3)
    age: int = Field(ge=18, le=100)
    # email: EmailStr  # Uncomment after: pip install pydantic[email]

@app.post("/product")
def add_product(product: Product):
    return {"added": product.name, "total": product.price * product.quantity}

@app.post("/signup")
def signup(user: UserSignup):
    return {"message": f"Welcome {user.username}"}

# Run: uvicorn validation:app --reload

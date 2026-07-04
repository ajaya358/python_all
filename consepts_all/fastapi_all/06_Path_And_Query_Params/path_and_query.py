from fastapi import FastAPI

app = FastAPI()

# Path param: /users/5
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# Path + query param: /products/3?discount=true
@app.get("/products/{product_id}")
def get_product(product_id: int, discount: bool = False):
    price = 100
    if discount:
        price = 80
    return {"product_id": product_id, "price": price}

# Multiple path params: /orders/2/items/5
@app.get("/orders/{order_id}/items/{item_id}")
def get_order_item(order_id: int, item_id: int):
    return {"order_id": order_id, "item_id": item_id}

# Run: uvicorn path_and_query:app --reload

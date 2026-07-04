# Service Communication - How microservices talk to each other

import httpx
import asyncio

# --- Synchronous HTTP call between services ---
print("=== Sync HTTP (httpx) ===")
print("""
import httpx

# User service calling Product service
def get_user_orders(user_id: int):
    # Call Order service
    response = httpx.get(f"http://order-service:8003/orders?user_id={user_id}")
    response.raise_for_status()
    return response.json()
""")

# --- Async HTTP call ---
print("=== Async HTTP (httpx async) ===")
print("""
import httpx
import asyncio

async def get_product_details(product_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://product-service:8002/products/{product_id}")
        return response.json()

# Call multiple services in parallel
async def get_order_with_details(order_id: int):
    async with httpx.AsyncClient() as client:
        order_resp, user_resp = await asyncio.gather(
            client.get(f"http://order-service:8003/orders/{order_id}"),
            client.get(f"http://user-service:8001/users/1"),
        )
    return {"order": order_resp.json(), "user": user_resp.json()}
""")

# --- Service simulation ---
print("=== Mini Microservices Simulation ===")

class UserService:
    users = {1: {"id": 1, "name": "Ajay"}, 2: {"id": 2, "name": "Ravi"}}
    def get_user(self, user_id):
        return self.users.get(user_id, {"error": "User not found"})

class OrderService:
    orders = {
        1: [{"product": "Laptop", "amount": 50000}],
        2: [{"product": "Phone", "amount": 20000}],
    }
    def get_orders(self, user_id):
        return self.orders.get(user_id, [])

class APIGateway:
    def __init__(self):
        self.user_svc = UserService()
        self.order_svc = OrderService()

    def get_user_with_orders(self, user_id):
        user = self.user_svc.get_user(user_id)
        orders = self.order_svc.get_orders(user_id)
        return {"user": user, "orders": orders}

gateway = APIGateway()
print(gateway.get_user_with_orders(1))
print(gateway.get_user_with_orders(2))

print("\n=== Retry with Timeout ===")
print("""
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
def call_service(url: str):
    response = httpx.get(url, timeout=5.0)
    response.raise_for_status()
    return response.json()
""")

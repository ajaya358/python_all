# API Gateway - Single entry point for all microservices
# Client talks to gateway, gateway routes to correct service

from fastapi import FastAPI, HTTPException, Request
import httpx

app = FastAPI(title="API Gateway")

# Service URLs (in production use env vars or service discovery)
SERVICES = {
    "users":    "http://localhost:8001",
    "products": "http://localhost:8002",
    "orders":   "http://localhost:8003",
}

# --- Generic proxy function ---
async def proxy_request(service_url: str, path: str, method: str, body=None, headers=None):
    async with httpx.AsyncClient() as client:
        url = f"{service_url}{path}"
        try:
            response = await client.request(
                method=method,
                url=url,
                json=body,
                headers=headers,
                timeout=10.0
            )
            return response.json(), response.status_code
        except httpx.ConnectError:
            raise HTTPException(status_code=503, detail=f"Service unavailable: {service_url}")
        except httpx.TimeoutException:
            raise HTTPException(status_code=504, detail="Service timeout")

# --- Gateway Routes ---
@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    data, status = await proxy_request(SERVICES["users"], f"/users/{user_id}", "GET")
    return data

@app.get("/api/products")
async def get_products(category: str = None):
    path = f"/products?category={category}" if category else "/products"
    data, status = await proxy_request(SERVICES["products"], path, "GET")
    return data

@app.post("/api/orders")
async def create_order(request: Request):
    body = await request.json()
    data, status = await proxy_request(SERVICES["orders"], "/orders", "POST", body)
    return data

# --- Aggregation: combine data from multiple services ---
@app.get("/api/dashboard/{user_id}")
async def get_dashboard(user_id: int):
    async with httpx.AsyncClient() as client:
        import asyncio
        user_task    = client.get(f"{SERVICES['users']}/users/{user_id}")
        orders_task  = client.get(f"{SERVICES['orders']}/orders?user_id={user_id}")
        user_r, orders_r = await asyncio.gather(user_task, orders_task, return_exceptions=True)
        return {
            "user":   user_r.json() if not isinstance(user_r, Exception) else None,
            "orders": orders_r.json() if not isinstance(orders_r, Exception) else [],
        }

print("=== API Gateway Responsibilities ===")
responsibilities = [
    "Route requests to correct service",
    "Authentication — verify JWT before forwarding",
    "Rate limiting — protect all services",
    "Load balancing — distribute traffic",
    "Request aggregation — combine multiple service responses",
    "Logging — log all incoming requests",
    "SSL termination — handle HTTPS",
]
for r in responsibilities:
    print(f"  - {r}")

# Run: uvicorn api_gateway:app --reload --port 8000

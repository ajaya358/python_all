# Docker Microservices - Run all services with docker-compose

print("=== Project Structure ===")
print("""
ecommerce/
├── gateway/
│   ├── main.py
│   └── Dockerfile
├── user_service/
│   ├── main.py
│   └── Dockerfile
├── product_service/
│   ├── main.py
│   └── Dockerfile
├── order_service/
│   ├── main.py
│   └── Dockerfile
└── docker-compose.yml
""")

print("=== docker-compose.yml ===")
print("""
version: '3.8'

services:
  gateway:
    build: ./gateway
    ports:
      - "8000:8000"
    depends_on:
      - user_service
      - product_service
      - order_service
    environment:
      - USER_SERVICE_URL=http://user_service:8001
      - PRODUCT_SERVICE_URL=http://product_service:8002
      - ORDER_SERVICE_URL=http://order_service:8003

  user_service:
    build: ./user_service
    ports:
      - "8001:8001"
    depends_on:
      - user_db
    environment:
      - DATABASE_URL=postgresql://user:pass@user_db:5432/users_db

  product_service:
    build: ./product_service
    ports:
      - "8002:8002"
    depends_on:
      - product_db

  order_service:
    build: ./order_service
    ports:
      - "8003:8003"
    depends_on:
      - order_db
      - redis

  user_db:
    image: postgres:15
    environment:
      POSTGRES_DB: users_db
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass

  product_db:
    image: postgres:15
    environment:
      POSTGRES_DB: products_db
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass

  order_db:
    image: postgres:15
    environment:
      POSTGRES_DB: orders_db
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass

  redis:
    image: redis:7
    ports:
      - "6379:6379"

networks:
  default:
    name: ecommerce_network
""")

print("=== Commands ===")
print("  docker-compose up --build     → start all services")
print("  docker-compose up -d          → run in background")
print("  docker-compose logs -f        → view all logs")
print("  docker-compose down           → stop all")
print("  docker-compose scale user_service=3  → run 3 instances")

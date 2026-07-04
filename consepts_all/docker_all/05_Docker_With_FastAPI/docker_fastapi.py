# Docker with FastAPI - Complete Setup Guide

print("=== Project Structure ===")
structure = """
fastapi_docker/
├── main.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
"""
print(structure)

print("=== main.py ===")
main_py = """
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Running inside Docker!"}

@app.get("/health")
def health():
    return {"status": "healthy"}
"""
print(main_py)

print("=== Dockerfile ===")
dockerfile = """
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""
print(dockerfile)

print("=== requirements.txt ===")
print("fastapi\nuvicorn\n")

print("=== docker-compose.yml ===")
compose = """
version: '3.8'
services:
  api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app        # live reload during development
    command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
"""
print(compose)

print("=== Commands to Run ===")
print("  docker-compose up --build   → build and start")
print("  docker-compose up -d        → run in background")
print("  docker-compose down         → stop everything")
print("  Open: http://localhost:8000")
print("  Docs: http://localhost:8000/docs")

print("\n=== Environment Variables in Docker ===")
env_example = """
# In docker-compose.yml
environment:
  - APP_ENV=production
  - SECRET_KEY=mysecret
  - DATABASE_URL=postgresql://user:pass@db:5432/mydb

# Or use .env file
env_file:
  - .env
"""
print(env_example)

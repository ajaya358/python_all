# Docker Compose - Run multiple containers together
# One docker-compose.yml file defines all services

print("=== What is Docker Compose? ===")
print("  Run app + database + redis + nginx all together")
print("  One command: docker-compose up")
print("  One command to stop: docker-compose down\n")

print("=== Docker Compose Commands ===")
commands = {
    "docker-compose up":          "Start all services",
    "docker-compose up -d":       "Start in background (detached)",
    "docker-compose down":        "Stop and remove containers",
    "docker-compose logs":        "View logs of all services",
    "docker-compose ps":          "List running services",
    "docker-compose build":       "Rebuild images",
    "docker-compose exec web sh": "Enter a running service",
}
for cmd, desc in commands.items():
    print(f"  {cmd:35} → {desc}")

print("\n=== docker-compose.yml (FastAPI + PostgreSQL) ===")
compose_content = """
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/mydb
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7
    ports:
      - "6379:6379"

volumes:
  postgres_data:
"""
print(compose_content)

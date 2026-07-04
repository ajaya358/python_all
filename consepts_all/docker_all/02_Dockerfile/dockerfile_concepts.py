# Dockerfile - Instructions to build a Docker image
# Each line = one layer in the image

print("=== Dockerfile Instructions ===")
instructions = {
    "FROM":       "Base image to start from",
    "WORKDIR":    "Set working directory inside container",
    "COPY":       "Copy files from host to container",
    "RUN":        "Execute command during build",
    "CMD":        "Default command when container starts",
    "EXPOSE":     "Document which port the app uses",
    "ENV":        "Set environment variables",
    "ARG":        "Build-time variables",
    "ENTRYPOINT": "Fixed command (CMD appends to it)",
}
for k, v in instructions.items():
    print(f"  {k:12}: {v}")

print("\n=== Dockerfile for Python/FastAPI App ===")
dockerfile_content = """
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""
print(dockerfile_content)

print("=== requirements.txt ===")
requirements = """
fastapi
uvicorn
"""
print(requirements)

print("=== Build & Run Commands ===")
print("  docker build -t fastapi-app .")
print("  docker run -p 8000:8000 fastapi-app")
print("  Open: http://localhost:8000")

print("\n=== Multi-stage Build (smaller image) ===")
multistage = """
# Stage 1: Build
FROM python:3.11 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Run (smaller base)
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""
print(multistage)

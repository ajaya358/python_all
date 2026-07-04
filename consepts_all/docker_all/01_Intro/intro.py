# Docker - Introduction
# Docker packages your app + dependencies into a container
# Container runs the same on any machine (dev, test, production)

print("=== What is Docker? ===")
concepts = {
    "Image":      "Blueprint of your app (like a class)",
    "Container":  "Running instance of an image (like an object)",
    "Dockerfile": "Instructions to build an image",
    "Registry":   "Store for images (Docker Hub, ECR, ACR)",
    "Volume":     "Persistent storage for containers",
    "Network":    "Communication between containers",
    "Compose":    "Run multi-container apps with one command",
}
for k, v in concepts.items():
    print(f"  {k}: {v}")

print("\n=== Docker vs Virtual Machine ===")
print("  VM:        Full OS + App  → Heavy (GBs), slow start")
print("  Container: Shared OS + App → Light (MBs), fast start")

print("\n=== Docker Workflow ===")
steps = [
    "1. Write your app (e.g., FastAPI)",
    "2. Write Dockerfile (build instructions)",
    "3. docker build -t myapp .        → creates image",
    "4. docker run -p 8000:8000 myapp  → starts container",
    "5. docker push myapp              → upload to registry",
]
for s in steps:
    print(f"  {s}")

print("\n=== Common Docker Commands ===")
commands = {
    "docker build -t name .":       "Build image from Dockerfile",
    "docker run -p 8000:8000 name": "Run container, map port",
    "docker ps":                    "List running containers",
    "docker ps -a":                 "List all containers",
    "docker stop <id>":             "Stop a container",
    "docker rm <id>":               "Remove a container",
    "docker images":                "List all images",
    "docker rmi <id>":              "Remove an image",
    "docker logs <id>":             "View container logs",
    "docker exec -it <id> bash":    "Enter running container",
}
for cmd, desc in commands.items():
    print(f"  {cmd:40} → {desc}")

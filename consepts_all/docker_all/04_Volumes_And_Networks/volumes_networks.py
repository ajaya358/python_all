# Docker Volumes and Networks

print("=== Volumes - Persistent Storage ===")
print("  Without volume: data is lost when container stops")
print("  With volume: data persists even after container restart\n")

volume_types = {
    "Named Volume":   "docker volume create mydata  → managed by Docker",
    "Bind Mount":     "-v /host/path:/container/path → maps host folder",
    "tmpfs Mount":    "Stored in memory only, not on disk",
}
for k, v in volume_types.items():
    print(f"  {k}: {v}")

print("\n=== Volume Commands ===")
vol_commands = {
    "docker volume create mydata":        "Create a named volume",
    "docker volume ls":                   "List all volumes",
    "docker volume inspect mydata":       "View volume details",
    "docker volume rm mydata":            "Remove a volume",
    "docker run -v mydata:/app/data img": "Mount volume to container",
}
for cmd, desc in vol_commands.items():
    print(f"  {cmd:45} → {desc}")

print("\n=== Networks - Container Communication ===")
network_types = {
    "bridge":  "Default. Containers on same host can talk",
    "host":    "Container shares host network (no isolation)",
    "none":    "No network access",
    "overlay": "Multi-host networking (Docker Swarm)",
}
for k, v in network_types.items():
    print(f"  {k:8}: {v}")

print("\n=== Network Commands ===")
net_commands = {
    "docker network create mynet":              "Create custom network",
    "docker network ls":                        "List networks",
    "docker network inspect mynet":             "View network details",
    "docker run --network mynet img":           "Connect container to network",
    "docker network connect mynet container1":  "Add container to network",
}
for cmd, desc in net_commands.items():
    print(f"  {cmd:48} → {desc}")

print("\n=== Example: Two containers talking ===")
example = """
# Both containers on same network can reach each other by service name
docker network create appnet
docker run -d --name db --network appnet postgres
docker run -d --name web --network appnet -e DB_HOST=db myapp
# 'web' container connects to 'db' using hostname 'db'
"""
print(example)

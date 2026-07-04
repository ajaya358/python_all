# Load Balancing - Distribute traffic across multiple servers

print("=== What is Load Balancing? ===")
print("  Distribute incoming requests across multiple servers")
print("  Prevents any single server from being overwhelmed\n")

print("=== Load Balancing Algorithms ===")
algorithms = {
    "Round Robin":          "Request 1→Server1, Request 2→Server2, Request 3→Server3, repeat",
    "Weighted Round Robin": "Server with more capacity gets more requests",
    "Least Connections":    "Send to server with fewest active connections",
    "IP Hash":              "Same client IP always goes to same server (sticky sessions)",
    "Random":               "Pick random server",
    "Least Response Time":  "Send to fastest responding server",
}
for k, v in algorithms.items():
    print(f"  {k:25}: {v}")

print("\n=== Load Balancer Types ===")
lb_types = {
    "Layer 4 (Transport)": "Routes based on IP/TCP — fast, no content inspection",
    "Layer 7 (Application)":"Routes based on URL, headers, cookies — smarter",
}
for k, v in lb_types.items():
    print(f"  {k:25}: {v}")

print("\n=== Load Balancer Tools ===")
tools = {
    "Nginx":        "Most popular, also web server, reverse proxy",
    "HAProxy":      "High performance, TCP and HTTP load balancing",
    "AWS ALB":      "AWS Application Load Balancer — Layer 7",
    "AWS NLB":      "AWS Network Load Balancer — Layer 4, ultra fast",
    "Traefik":      "Cloud-native, auto-discovers Docker/K8s services",
}
for k, v in tools.items():
    print(f"  {k:12}: {v}")

print("\n=== Nginx Load Balancer Config ===")
print("""
# /etc/nginx/nginx.conf
upstream backend {
    least_conn;                          # algorithm
    server 192.168.1.10:8000 weight=3;  # gets 3x more traffic
    server 192.168.1.11:8000 weight=1;
    server 192.168.1.12:8000 backup;    # only used if others fail
}

server {
    listen 80;
    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
""")

print("=== Health Checks ===")
print("  Load balancer pings /health endpoint every 30 seconds")
print("  If server fails → removed from pool automatically")
print("  When server recovers → added back to pool")

# --- Simple round-robin simulation ---
print("\n=== Round Robin Simulation ===")
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

lb = LoadBalancer(["Server1:8001", "Server2:8002", "Server3:8003"])
for i in range(6):
    print(f"  Request {i+1} → {lb.get_server()}")

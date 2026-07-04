# Linux Networking Commands - Essential for backend developers

print("=== Check Network ===")
net_cmds = {
    "ip addr":                      "Show IP addresses of all interfaces",
    "ifconfig":                     "Show network interfaces (older)",
    "hostname -I":                  "Show server IP address",
    "ping google.com":              "Test connectivity",
    "ping -c 4 google.com":         "Ping 4 times only",
    "traceroute google.com":        "Show network path to host",
    "nslookup google.com":          "DNS lookup",
    "dig google.com":               "Detailed DNS lookup",
    "curl ifconfig.me":             "Get your public IP",
}
for cmd, desc in net_cmds.items():
    print(f"  {cmd:35}: {desc}")

print("\n=== Ports and Connections ===")
port_cmds = {
    "netstat -tulpn":               "List all open ports and services",
    "ss -tulpn":                    "Modern version of netstat",
    "lsof -i :8000":                "What is using port 8000",
    "lsof -i :5432":                "What is using PostgreSQL port",
    "fuser 8000/tcp":               "PID using port 8000",
}
for cmd, desc in port_cmds.items():
    print(f"  {cmd:35}: {desc}")

print("\n=== curl - Test APIs from Terminal ===")
curl_cmds = {
    "curl http://localhost:8000":                           "GET request",
    "curl -X POST http://localhost:8000/users":             "POST request",
    'curl -X POST -H "Content-Type: application/json" -d \'{"name":"Ajay"}\' http://localhost:8000/users': "POST with JSON",
    'curl -H "Authorization: Bearer <token>" http://localhost:8000/me': "With auth header",
    "curl -o output.json http://api.example.com/data":      "Save response to file",
}
for cmd, desc in curl_cmds.items():
    print(f"  {cmd[:60]:60}: {desc}")

print("\n=== SSH - Connect to Remote Server ===")
ssh_cmds = {
    "ssh ubuntu@192.168.1.100":             "Connect to server",
    "ssh -i key.pem ubuntu@server_ip":      "Connect with key file",
    "scp file.txt ubuntu@server:/home/":    "Copy file to server",
    "scp ubuntu@server:/home/file.txt .":   "Copy file from server",
    "ssh-keygen -t rsa":                    "Generate SSH key pair",
}
for cmd, desc in ssh_cmds.items():
    print(f"  {cmd:45}: {desc}")

print("\n=== Firewall (UFW) ===")
ufw_cmds = {
    "sudo ufw status":          "Check firewall status",
    "sudo ufw allow 8000":      "Open port 8000",
    "sudo ufw allow ssh":       "Allow SSH (port 22)",
    "sudo ufw deny 3306":       "Block MySQL port",
    "sudo ufw enable":          "Enable firewall",
}
for cmd, desc in ufw_cmds.items():
    print(f"  {cmd:30}: {desc}")

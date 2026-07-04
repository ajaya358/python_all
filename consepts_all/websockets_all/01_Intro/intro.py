# WebSockets - Real-time two-way communication
# pip install fastapi uvicorn websockets

print("=== What is WebSocket? ===")
concepts = {
    "WebSocket":      "Persistent two-way connection between client and server",
    "HTTP":           "Request → Response → Connection closed (one-way, short-lived)",
    "WebSocket":      "Connect once → send/receive anytime (two-way, persistent)",
    "ws://":          "WebSocket URL (like http://)",
    "wss://":         "Secure WebSocket (like https://)",
    "Handshake":      "Starts as HTTP, upgrades to WebSocket protocol",
    "Frame":          "Unit of data sent over WebSocket",
    "Ping/Pong":      "Keep-alive mechanism to detect disconnected clients",
}
for k, v in concepts.items():
    print(f"  {k:14}: {v}")

print("\n=== HTTP vs WebSocket ===")
print("""
  HTTP (REST):
    Client → Request  → Server
    Client ← Response ← Server
    Connection closed. Client must poll for updates.

  WebSocket:
    Client ←→ Server  (connection stays open)
    Server can push data anytime without client asking
""")

print("=== Use Cases ===")
use_cases = [
    "Chat applications (WhatsApp, Slack)",
    "Live notifications (order status, alerts)",
    "Real-time dashboards (stock prices, analytics)",
    "Multiplayer games",
    "Collaborative editing (Google Docs)",
    "Live sports scores",
    "IoT device data streaming",
]
for u in use_cases:
    print(f"  - {u}")

print("\n=== Install ===")
print("  pip install fastapi uvicorn websockets")
print("  Test with: wscat -c ws://localhost:8000/ws")
print("  Install wscat: npm install -g wscat")

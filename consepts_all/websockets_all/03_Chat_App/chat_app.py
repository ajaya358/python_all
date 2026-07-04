# WebSocket Chat App - Multiple users, broadcast messages
# pip install fastapi uvicorn
# Run: uvicorn chat_app:app --reload

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict
import json

app = FastAPI()

# --- Connection Manager ---
class ConnectionManager:
    def __init__(self):
        self.connections: Dict[str, WebSocket] = {}  # username → websocket

    async def connect(self, username: str, websocket: WebSocket):
        await websocket.accept()
        self.connections[username] = websocket
        await self.broadcast({"type": "join", "user": username, "message": f"{username} joined the chat"})

    async def disconnect(self, username: str):
        if username in self.connections:
            del self.connections[username]
            await self.broadcast({"type": "leave", "user": username, "message": f"{username} left the chat"})

    async def send_to(self, username: str, data: dict):
        if username in self.connections:
            await self.connections[username].send_json(data)

    async def broadcast(self, data: dict):
        for ws in self.connections.values():
            await ws.send_json(data)

    def get_online_users(self):
        return list(self.connections.keys())

manager = ConnectionManager()

# --- Chat WebSocket endpoint ---
@app.websocket("/chat/{username}")
async def chat(websocket: WebSocket, username: str):
    await manager.connect(username, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)

            if message.get("type") == "private":
                # Private message to specific user
                await manager.send_to(
                    message["to"],
                    {"type": "private", "from": username, "message": message["message"]}
                )
            else:
                # Broadcast to all
                await manager.broadcast({
                    "type": "message",
                    "user": username,
                    "message": message.get("message", data)
                })
    except WebSocketDisconnect:
        await manager.disconnect(username)

@app.get("/online")
def online_users():
    return {"users": manager.get_online_users(), "count": len(manager.connections)}

# Run: uvicorn chat_app:app --reload
# Connect user1: wscat -c ws://localhost:8000/chat/Ajay
# Connect user2: wscat -c ws://localhost:8000/chat/Ravi
# Send message: {"message": "Hello everyone!"}
# Private msg:  {"type": "private", "to": "Ravi", "message": "Hi Ravi!"}

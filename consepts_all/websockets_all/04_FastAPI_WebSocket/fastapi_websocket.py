# FastAPI WebSocket - Rooms + Authentication
# pip install fastapi uvicorn
# Run: uvicorn fastapi_websocket:app --reload

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query, HTTPException
from typing import Dict, List
import json

app = FastAPI()

# --- Room-based Connection Manager ---
class RoomManager:
    def __init__(self):
        self.rooms: Dict[str, Dict[str, WebSocket]] = {}  # room → {username: ws}

    async def join_room(self, room: str, username: str, websocket: WebSocket):
        await websocket.accept()
        if room not in self.rooms:
            self.rooms[room] = {}
        self.rooms[room][username] = websocket
        await self.broadcast_room(room, {
            "type": "join", "user": username,
            "message": f"{username} joined room '{room}'",
            "online": list(self.rooms[room].keys())
        })

    async def leave_room(self, room: str, username: str):
        if room in self.rooms and username in self.rooms[room]:
            del self.rooms[room][username]
            if not self.rooms[room]:
                del self.rooms[room]
            else:
                await self.broadcast_room(room, {
                    "type": "leave", "user": username,
                    "message": f"{username} left room '{room}'"
                })

    async def broadcast_room(self, room: str, data: dict):
        if room in self.rooms:
            for ws in self.rooms[room].values():
                await ws.send_json(data)

    def get_rooms(self):
        return {room: list(users.keys()) for room, users in self.rooms.items()}

manager = RoomManager()

# --- Simple token auth for WebSocket ---
VALID_TOKENS = {"token123": "Ajay", "token456": "Ravi", "token789": "Priya"}

def authenticate(token: str) -> str:
    username = VALID_TOKENS.get(token)
    if not username:
        raise HTTPException(status_code=403, detail="Invalid token")
    return username

# --- WebSocket with room and auth ---
@app.websocket("/ws/{room}")
async def room_chat(
    websocket: WebSocket,
    room: str,
    token: str = Query(...)
):
    try:
        username = authenticate(token)
    except HTTPException:
        await websocket.close(code=4001)
        return

    await manager.join_room(room, username, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            msg = json.loads(data)
            await manager.broadcast_room(room, {
                "type": "message",
                "user": username,
                "room": room,
                "message": msg.get("message", "")
            })
    except WebSocketDisconnect:
        await manager.leave_room(room, username)

@app.get("/rooms")
def list_rooms():
    return manager.get_rooms()

# Run: uvicorn fastapi_websocket:app --reload
# Connect: wscat -c "ws://localhost:8000/ws/general?token=token123"
# Send: {"message": "Hello room!"}

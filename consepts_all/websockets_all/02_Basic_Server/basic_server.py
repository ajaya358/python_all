# Basic WebSocket Server with FastAPI
# pip install fastapi uvicorn
# Run: uvicorn basic_server:app --reload
# Test: wscat -c ws://localhost:8000/ws

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

# --- Basic echo server ---
@app.websocket("/ws")
async def websocket_echo(websocket: WebSocket):
    await websocket.accept()
    print("Client connected")
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received: {data}")
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")

# --- Send JSON data ---
@app.websocket("/ws/json")
async def websocket_json(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            print(f"Received JSON: {data}")
            response = {"status": "received", "data": data, "processed": True}
            await websocket.send_json(response)
    except WebSocketDisconnect:
        print("Client disconnected")

# --- Send data from server to client (push) ---
import asyncio

@app.websocket("/ws/live-data")
async def live_data(websocket: WebSocket):
    await websocket.accept()
    try:
        count = 0
        while True:
            count += 1
            await websocket.send_json({"count": count, "message": f"Update #{count}"})
            await asyncio.sleep(1)  # push every 1 second
    except WebSocketDisconnect:
        print("Client disconnected")

# --- HTTP endpoint to test server is running ---
@app.get("/")
def root():
    return {"message": "WebSocket server running", "endpoints": ["/ws", "/ws/json", "/ws/live-data"]}

# Run: uvicorn basic_server:app --reload
# Connect: wscat -c ws://localhost:8000/ws
# Then type any message and see echo response

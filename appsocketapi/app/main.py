from typing import Union

from fastapi import FastAPI, WebSocket
from dapr.clients import DaprClient
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    data = await websocket.receive_text()
    await websocket.send_text(f"You sent: {data}")

@app.websocket("/ws/hello")
async def hello_websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    data = await websocket.receive_text()
    await websocket.send_text(f"Hello from sockets... You sent: {data}")

@app.websocket("/ws/world")
async def world_websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    data = await websocket.receive_text()
    await websocket.send_text(f"World from sockets... You sent: {data}")
import asyncio
from websockets.sync.client import connect

URI="ws://localhost:5080/ws"

def hello():
    with connect(URI) as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")

    with connect(URI + "/hello") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")

    with connect(URI + "/world") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")

hello()
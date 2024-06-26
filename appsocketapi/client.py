import asyncio
from websockets.sync.client import connect

#URI="ws://localhost:5080/ws"


URI="wss://apim-quackersbankl6ht6vt8.azure-api.net/websocket"
#URI="wss://socketapi.happygrass-f1771e78.eastus.azurecontainerapps.io/ws"
def hello():
    with connect(URI) as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")

    with connect(URI + "?channel=hello") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")

    with connect(URI + "?channel=world") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")

hello()
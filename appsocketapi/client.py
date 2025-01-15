import asyncio
from websockets.sync.client import connect

#URI="ws://localhost:5080/ws"


#URI="wss://apim-quackersbankl6ht6vt8.azure-api.net/websocket"
URI="wss://acabasicapi-audccjgkaeaya7cm.b02.azurefd.net/ws/ws"
#URI="wss://socketapi.happygrass-f1771e78.eastus.azurecontainerapps.io/ws"
def hello():
    print(URI)
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

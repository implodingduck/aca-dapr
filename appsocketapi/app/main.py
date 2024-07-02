from typing import Union
from azure.identity import ManagedIdentityCredential
from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import RedirectResponse
import json
import os
import requests

managed_identity_client_id = os.environ.get("MANAGED_IDENTITY_CLIENT_ID")
api_uri = os.environ.get("API_URI")
test_endpoint = os.environ.get("TEST_ENDPOINT")

credential = ManagedIdentityCredential(client_id=managed_identity_client_id)
token = credential.get_token(f"{api_uri}/.default")

redirecttest = os.environ.get("REDIRECT_TEST")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print("/ws")
    await websocket.accept()
    data = await websocket.receive_text()
    await websocket.send_text(f"You sent: {data}")

@app.websocket("/ws/hello")
async def hello_websocket_endpoint(websocket: WebSocket):
    print("/ws/hello")
    await websocket.accept()
    data = await websocket.receive_text()
    await websocket.send_text(f"Hello from sockets... You sent: {data}")

@app.websocket("/ws/world")
async def world_websocket_endpoint(websocket: WebSocket):
    print("/ws/world")
    await websocket.accept()
    data = await websocket.receive_text()
    await websocket.send_text(f"World from sockets... You sent: {data}")


@app.get("/mitest")
def get_mitest():
    
    headers = {
        "Authorization": f"Bearer {token.token}"
    }
    resp1 = requests.get(test_endpoint)
    resp2 = requests.get(test_endpoint, headers=headers)
    
    return {"resp1": {
        "status": resp1.status_code,
        "text": resp1.text
    }, "resp2": {
        "status": resp2.status_code,
        "text": resp2.text
    }, "token": token.token
    }

@app.get("/redirecttest")
def get_redirecttest(request: Request):
    return RedirectResponse(url=redirecttest, status_code=302)

@app.get("/redirecttarget")
def get_redirecttest(request: Request):
    return {
        "Hello": "Redirect",
        "headers": request.headers
    }
from typing import Union

from fastapi import FastAPI
from dapr.clients import DaprClient
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/calltimer")
def call_timer(duration: Union[int, None] = None):
    with DaprClient() as d:
        resp = d.invoke_method('timerapi', f'timeout/{duration}')
    return { "resp": resp.text() }
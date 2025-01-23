from typing import Union

from fastapi import FastAPI, Request
from dapr.clients import DaprClient
import json
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/appconfig")
def read_appconfig():
    keys = os.environ.get('APP_CONFIG_KEYS', 'hello').split(',')
    store = os.environ.get('APP_CONFIG_STORE_NAME', '')
    with DaprClient() as d:
        configuration = d.get_configuration(store_name=store, keys=keys)
    return { "configuration": configuration, "store": store, "keys": keys }
    

@app.get("/me")
def me(request: Request):
    return {"headers": request.headers}
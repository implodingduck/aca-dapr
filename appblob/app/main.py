from typing import Union

from fastapi import FastAPI, Request
from dapr.clients import DaprClient
import json
import uuid
import datetime
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/me")
def me(request: Request):
    return {"headers": request.headers}

@app.get("/create")
def output_binding_create():
    with DaprClient() as d:
        resp = d.invoke_binding('outputbinding', 'create', data=f"{datetime.datetime.now()} - {uuid.uuid4()}\n", binding_metadata={ "blobName": "myblob.txt"})
    return {"resp": resp.text()}

@app.get("/read")
def output_binding_read():
    with DaprClient() as d:
        resp = d.invoke_binding('outputbinding', 'get', binding_metadata={ "blobName": "myblob.txt", "includeMetadata": "true"})
    return {"resp": resp.text()}
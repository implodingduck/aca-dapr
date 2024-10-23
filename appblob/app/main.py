from typing import Union

from fastapi import FastAPI, Request

import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/me")
def me(request: Request):
    return {"headers": request.headers}
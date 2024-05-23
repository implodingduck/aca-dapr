from typing import Union

from fastapi import FastAPI

import time
import datetime

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/timeout/")
def timeout(duration: Union[int, None] = None):
    start = datetime.datetime.now()
    time.sleep(duration)
    end = datetime.datetime.now()
    return {"duration": duration, "starttime": start, "endtime": end}
from fastapi import FastAPI, Request
import base64
import time
import datetime

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/dapr/subscribe")
async def subscribe():
    subscriptions = [{'pubsubname': 'pubsub',
                      'topic': 'deathstarstatus',
                      'route': 'dsstatus',
                      'metadata': {
                          'rawPayload': 'true',
                      } }]
    print(f"Returning subscriptions: {subscriptions}")
    return subscriptions


@app.post("/dsstatus")
async def dsstatus(request: Request):
    req_json = await request.json()
    print("-----------------")
    print(f"Received: {req_json}")
    data = base64.b64decode(req_json['data_base64'])
    print(f"data: {data}")
    print(f"headers: {request.headers}")
    if str(data)=="triggerdelay":    
        print(f"Delaying: {datetime.datetime.now()}")
        time.sleep(360)
        print(f"Done: {datetime.datetime.now()}")
        
    return req_json
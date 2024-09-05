from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/dapr/subscribe")
async def subscribe():
    subscriptions = [{'pubsubname': 'pubsub',
                      'queue': 'deathstarstatus',
                      'route': 'dsstatus',
                      'metadata': {
                          'rawPayload': 'true',
                      } }]
    print(f"Returning subscriptions: {subscriptions}")
    return subscriptions


@app.post("/dsstatus")
async def dsstatus(request: Request):
    req_json = await request.json()
    print(f"Received: {req_json}")
    return req_json
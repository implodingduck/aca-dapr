from dapr.clients import DaprClient

def call_timer(duration=5):
    with DaprClient() as d:
        resp = d.invoke_method('timerapi', f'timeout/{duration}')
    return { "resp": resp.text() }

print("Hello world!")
print(call_timer(5))
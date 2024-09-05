import os
from azure.servicebus import ServiceBusClient, ServiceBusMessage

conn_str = os.environ['SB_CONN_STR']
queue_name = "deathstarstatus"

with ServiceBusClient.from_connection_string(conn_str) as client:
    with client.get_queue_sender(queue_name) as sender:
        # Sending a single message
        single_message = ServiceBusMessage("Single message")
        sender.send_messages(single_message)

        # Sending a list of messages
        messages = [ServiceBusMessage("First message"), ServiceBusMessage("Second message")]
        sender.send_messages(messages)

print("Done!")

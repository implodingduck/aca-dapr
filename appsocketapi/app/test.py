from azure.identity import ManagedIdentityCredential
import os
import requests

managed_identity_client_id = os.environ.get("MANAGED_IDENTITY_CLIENT_ID")
api_uri = os.environ.get("API_URI")
test_endpoint = os.environ.get("TEST_ENDPOINT")

resp = requests.get(test_endpoint)
print(resp)

credential = ManagedIdentityCredential(client_id=managed_identity_client_id)
token = credential.get_token(f"{api_uri}/.default")
print(token)

headers = {
    "Authorization": f"Bearer {token.token}"
}

resp = requests.get(test_endpoint, headers=headers)
print(resp)
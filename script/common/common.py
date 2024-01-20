import requests
import json

def http_get_response_data(url: str) -> dict:
     response = requests.get(url)
     return json.loads(response.text)
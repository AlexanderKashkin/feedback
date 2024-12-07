import requests
import json


def test():
    url = "http://127.0.0.1:8000/sign-form"

    payload = json.dumps({
        "token": "112",
        "name": "Alexander",
        "phone": "+7981320625"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    for i in range(300):
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)

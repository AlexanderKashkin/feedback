import requests
import json


def test():
    url = "http://127.0.0.1:8000/sign-form"

    payload1 = json.dumps({
        "token": "112",
        "name": "Alexander",
        "phone": "+7981320625"
    })
    payload2 = json.dumps({
        "token": "123",
        "name": "Alexander",
        "phone": "79818320625",
        "msg": "dgdgdfgdfgdfgdfgdffffffffffffffff"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    for i in range(300):
        response = requests.request("POST", url, headers=headers, data=payload1)
        response = requests.request("POST", url, headers=headers, data=payload1)
        print(response.text)

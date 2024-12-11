import requests
import json

def test():
    url1 = "http://127.0.0.1:8000/sign-form"
    url2 = "http://127.0.0.1:8000/feedback"

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
        response1 = requests.request("POST", url1, headers=headers, data=payload1)
        response2 = requests.request("POST", url2, headers=headers, data=payload2)
        print(response1.text)
        print(response2.text)
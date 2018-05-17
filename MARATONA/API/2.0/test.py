import json
import requests

url = "https://api.urionlinejudge.com.br/applications/token"

data = {
    'email': "lucasteixeirag11@gmail.com",
    'password': "blurs3Gambol73ensurers"
}

headers = {
    'content-type': "application/json",
    'accept': "application/json"
}

response = requests.request("POST", url, data=json.dumps(data), headers=headers)

print response.text